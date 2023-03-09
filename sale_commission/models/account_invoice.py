# -*- coding: utf-8 -*-

from odoo import api, fields, models


class AccountInvoice(models.Model):
    """Invoice inherit to add salesman"""
    _inherit = "account.invoice"

    @api.depends('invoice_line_ids.agents.amount')
    def _compute_commission_total(self):
        for record in self:
            record.commission_total = 0.0
            for line in record.invoice_line_ids:
                record.commission_total += sum(x.amount for x in line.agents)

    commission_total = fields.Float(
        string="Commissions", compute="_compute_commission_total",
        store=True, copy=False)

    @api.multi
    def action_cancel(self):
        """Put settlements associated to the invoices in exception."""
        settlements = self.env['sale.commission.settlement'].search(
            [('invoice', 'in', self.ids)])
        settlements.write({'state': 'except_invoice'})
        return super(AccountInvoice, self).action_cancel()

    @api.multi
    def invoice_validate(self):
        """Put settlements associated to the invoices again in invoice."""
        settlements = self.env['sale.commission.settlement'].search(
            [('invoice', 'in', self.ids)])
        settlements.write({'state': 'invoiced'})
        return super(AccountInvoice, self).invoice_validate()

    @api.multi
    def _refund_cleanup_lines(self, lines):
        """ugly function to map all fields of account.invoice.line
        when creates refund invoice"""
        res = super(AccountInvoice, self)._refund_cleanup_lines(lines)
        if lines and lines[0]._name != 'account.invoice.line':
            return res
        for i, line in enumerate(lines):
            vals = res[i][2]
            agents = super(AccountInvoice, self)._refund_cleanup_lines(
                line['agents'])
            # Remove old reference to source invoice
            for agent in agents:
                agent_vals = agent[2]
                del agent_vals['invoice']
                del agent_vals['invoice_line']
            vals['agents'] = agents
        return res

    @api.onchange('partner_id', 'company_id')
    def _onchange_partner_id(self):
        self.ensure_one()
        res = super(AccountInvoice, self)._onchange_partner_id()
        # workaround for https://github.com/odoo/odoo/issues/17618
        for line in self.invoice_line_ids:
            line.reval_commission = True
        return res

    @api.onchange('journal_id')
    def _onchange_journal_id(self):
        self.ensure_one()
        res = super(AccountInvoice, self)._onchange_journal_id()
        # workaround for https://github.com/odoo/odoo/issues/17618
        for line in self.invoice_line_ids:
            line.reval_commission = True
        return res

    @api.onchange('fiscal_position_id', 'payment_term_id', 'date_invoice')
    def _onchange_payment_term_date_invoice(self):
        self.ensure_one()
        res = super(AccountInvoice, self)._onchange_payment_term_date_invoice()
        if not self.env.context.get('skip_agents_delete'):
            # workaround for https://github.com/odoo/odoo/issues/17618
            for line in self.invoice_line_ids:
                line.reval_commission = True
        return res

    @api.multi
    def action_date_assign(self):
        # this is needed because action_date_assign calls
        # _onchange_payment_term_date_invoice to write to DB
        return super(AccountInvoice, self.with_context({
            'skip_agents_delete': True
        })).action_date_assign()

    @api.model
    def _recompute_lines_agents(self):
        for line in self.invoice_line_ids:
            line.agents = line._prepare_line_agents(self.partner_id._line_agents())
            line.reval_commission = False

    @api.multi
    def recompute_lines_agents(self):
        for invoice in self:
            invoice._recompute_lines_agents()


class AccountInvoiceLine(models.Model):
    _inherit = "account.invoice.line"

    @api.model
    def _default_agents(self):
        return self.get_commission_values(
            {'reval_commission': True}).get('agents') or []

    agents = fields.One2many(
        string="Agents & commissions",
        comodel_name="account.invoice.line.agent", inverse_name="invoice_line",
        help="Agents/Commissions related to the invoice line.",
        copy=True,
        default=_default_agents)
    commission_free = fields.Boolean(
        string="Comm. free", related="product_id.commission_free",
        store=True, readonly=True)
    reval_commission = fields.Boolean(
        string="Set Default Commission")

    @api.model
    def _prepare_line_agents(self, agents):
        # Issue https://github.com/odoo/odoo/issues/17618
        values = []
        agent_ids = [x.id for x in self.agents]
        for agent in agents:
            if isinstance(agent, dict):
                agent_vals = agent
            else:
                agent_vals = {
                    "agent": agent.id,
                    "commission": agent.commission.id
                }
            if agent_ids:
                rec_id = agent_ids.pop(0)
                values.append((1, rec_id, agent_vals))
            else:
                values.append((0, 0, agent_vals))
        if agent_ids:
            for rec_id in agent_ids:
                values.append((2, rec_id))
        return values

    @api.multi
    def set_line_agents(self, agents):
        for line in self:
            line.agents = line._prepare_line_agents(agents)
            line.reval_commission = False

    @api.multi
    def _prepare_invoice_line(self, qty):
        vals = super(AccountInvoiceLine, self)._prepare_invoice_line(qty)
        vals['agents'] = [
            (0, 0, {'agent': x.agent.id,
                    'commission': x.commission.id}) for x in self.agents]
        return vals

    @api.onchange('product_id')
    def product_id_change(self):
        self.agents = self._prepare_line_agents(
            self.invoice_id.partner_id._line_agents())
        self.reval_commission = False

    @api.model
    def _unbug_agents(self, agents):
        new_agents = []
        for item in agents:
            if isinstance(item, (list, tuple)):
                if item[0] == 5:
                    continue
                elif item[0] == 4:
                    rec_id = item[1]
                    rec = self.env["sale.order.line.agent"].browse(rec_id)
                    new_agents.append((1, rec_id, {
                        "agent": rec.agent.id,
                        "commission": rec.commission.id
                    }))
                else:
                    new_agents.append(item)
            else:
                new_agents.append(item)
        return new_agents

    @api.model
    def get_commission_values(self, vals):
        invoice_model = self.env['account.invoice']
        partner_model = self.env['res.partner']
        product_model = self.env['product.product']
        if self.env.context.get('partner_id'):
            partner = partner_model.browse(self.env.context['partner_id'])
        elif vals.get('invoice_id'):
            partner = invoice_model.browse(vals['invoice_id']).partner_id
        elif self.invoice_id:
            partner = self.invoice_id.partner_id
        else:
            partner = None
        if partner and vals.get('reval_commission'):
            if vals.get('product_id'):
                product = product_model.browse(vals['product_id'])
            elif self.product_id:
                product = self.product_id
            else:
                product = None
            if product:
                vals['commission_free'] = product.commission_free
            if not vals.get('commission_free'):
                vals["agents"] = self._prepare_line_agents(partner._line_agents())
        elif "agents" in vals:
            # Issue https://github.com/odoo/odoo/issues/17618
            vals["agents"] = self._unbug_agents(vals["agents"])
        vals['reval_commission'] = False
        return vals

    @api.multi
    def write(self, vals):
        vals = self.get_commission_values(vals)
        return super(AccountInvoiceLine, self).write(vals)

    @api.model
    def create(self, vals):
        vals = self.get_commission_values(vals)
        return super(AccountInvoiceLine, self).create(vals)


class AccountInvoiceLineAgent(models.Model):
    _name = "account.invoice.line.agent"

    invoice_line = fields.Many2one(
        comodel_name="account.invoice.line",
        ondelete="cascade",
        required=True, copy=False)
    invoice = fields.Many2one(
        string="Invoice", comodel_name="account.invoice",
        related="invoice_line.invoice_id",
        store=True)
    invoice_date = fields.Date(
        string="Invoice date",
        related="invoice.date_invoice",
        store=True, readonly=True)
    product = fields.Many2one(
        comodel_name='product.product',
        related="invoice_line.product_id")
    agent = fields.Many2one(
        comodel_name="res.partner",
        domain="[('agent', '=', True)]",
        ondelete="restrict",
        required=True)
    commission = fields.Many2one(
        comodel_name="sale.commission", ondelete="restrict", required=True)
    amount = fields.Float(
        string="Amount settled", compute="_compute_amount", store=True)
    agent_line = fields.Many2many(
        comodel_name='sale.commission.settlement.line',
        relation='settlement_agent_line_rel',
        column1='agent_line_id', column2='settlement_id',
        copy=False)
    settled = fields.Boolean(
        compute="_compute_settled",
        store=True, copy=False)
    company_id = fields.Many2one(
        related='invoice.company_id', store=True, readonly=True)
    currency_id = fields.Many2one(
        related='invoice.currency_id', store=True, readonly=True)
    inv_line_subtotal = fields.Monetary(
        string='Line Amount',
        # compute="_compute_subtotal")
        compute="_compute_amount")

    @api.onchange('agent')
    def onchange_agent(self):
        self.commission = self.agent.commission

    @api.depends('invoice_line.price_subtotal')
    def _compute_amount(self):
        for line in self:
            line.amount = 0.0
            line.inv_line_subtotal = line.invoice_line.price_subtotal
            if (not line.invoice_line.product_id.commission_free and
                    line.commission):
                if line.commission.amount_base_type == 'net_amount':
                    subtotal = (line.invoice_line.price_subtotal -
                                (line.invoice_line.product_id.standard_price *
                                 line.invoice_line.quantity))
                else:
                    subtotal = line.invoice_line.price_subtotal
                if line.commission.commission_type == 'fixed':
                    line.amount = subtotal * (line.commission.fix_qty / 100.0)
                else:
                    line.amount = line.commission.calculate_section(subtotal)
                # Refunds commissions are negative
                if line.invoice.type in ('out_refund', 'in_refund'):
                    line.amount = -line.amount

    @api.depends('agent_line', 'agent_line.settlement.state', 'invoice',
                 'invoice.state')
    def _compute_settled(self):
        # Count lines of not open or paid invoices as settled for not
        # being included in settlements
        for line in self:
            line.settled = (line.invoice.state not in ('open', 'paid') or
                            any(x.settlement.state != 'cancel'
                                for x in line.agent_line))

    _sql_constraints = [
        ('unique_agent', 'UNIQUE(invoice_line, agent)',
         'You can only add one time each agent.')
    ]
