# -*- coding: utf-8 -*-

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.depends('order_line.agents.amount')
    def _compute_commission_total(self):
        for record in self:
            record.commission_total = 0.0
            for line in record.order_line:
                record.commission_total += sum(x.amount for x in line.agents)

    commission_total = fields.Float(
        string="Commissions", compute="_compute_commission_total",
        store=True, copy=False)

    @api.onchange('partner_id', 'company_id')
    def onchange_partner_id(self):
        self.ensure_one()
        res = super(SaleOrder, self).onchange_partner_id()
        # workaround for https://github.com/odoo/odoo/issues/17618
        for line in self.order_line:
            line.reval_commission = True
        return res

    @api.onchange('fiscal_position_id', 'payment_term_id', 'date_invoice')
    def _compute_tax_id(self):
        self.ensure_one()
        res = super(SaleOrder, self)._compute_tax_id()
        # workaround for https://github.com/odoo/odoo/issues/17618
        for order_line in self.order_line:
            order_line.reval_commission = True
        return res

    @api.model
    def _prepare_line_agents_data(self):
        rec = []
        for agent in self.partner_id.agents:
            rec.append({
                'agent': agent.id,
                'commission': agent.commission.id,
            })
        return rec

    @api.model
    def _recompute_lines_agents(self):
        for line in self.order_line:
            line.agents = line._prepare_line_agents(self.partner_id._line_agents())
            line.reval_commission = False

    @api.multi
    def recompute_lines_agents(self):
        for order in self:
            order._recompute_lines_agents()


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.model
    def _default_agents(self):
        return self.get_commission_values(
            {'reval_commission': True}).get('agents') or []

    agents = fields.One2many(
        string="Agents & commissions",
        comodel_name="sale.order.line.agent", inverse_name="sale_line",
        help="Agents/Commissions related to the sale order line.",
        copy=True, readonly=True,
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
        vals = super(SaleOrderLine, self)._prepare_invoice_line(qty)
        vals['agents'] = [
            (0, 0, {'agent': x.agent.id,
                    'commission': x.commission.id}) for x in self.agents]
        return vals

    @api.onchange('product_id')
    def product_id_change(self):
        res = super(SaleOrderLine, self).product_id_change()
        self.agents = self._prepare_line_agents(self.order_id.partner_id._line_agents())
        self.reval_commission = False
        return res

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
        sale_order_model = self.env['sale.order']
        partner_model = self.env['res.partner']
        product_model = self.env['product.product']
        if self.env.context.get('partner_id'):
            partner = partner_model.browse(self.env.context['partner_id'])
        elif vals.get('order_id'):
            partner = sale_order_model.browse(vals['order_id']).partner_id
        elif self.order_id:
            partner = self.order_id.partner_id
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
        return super(SaleOrderLine, self).write(vals)

    @api.model
    def create(self, vals):
        vals = self.get_commission_values(vals)
        return super(SaleOrderLine, self).create(vals)


class SaleOrderLineAgent(models.Model):
    _name = "sale.order.line.agent"
    _rec_name = "agent"

    sale_line = fields.Many2one(
        comodel_name="sale.order.line",
        ondelete="cascade",
        required=True, copy=False)
    agent = fields.Many2one(
        comodel_name="res.partner", required=True, ondelete="restrict",
        domain="[('agent', '=', True')]")
    commission = fields.Many2one(
        comodel_name="sale.commission", required=True, ondelete="restrict")
    amount = fields.Float(compute="_compute_amount", store=True)

    _sql_constraints = [
        ('unique_agent', 'UNIQUE(sale_line, agent)',
         'You can only add one time each agent.')
    ]

    @api.onchange('agent')
    def onchange_agent(self):
        self.commission = self.agent.commission

    @api.depends('sale_line.price_subtotal')
    def _compute_amount(self):
        for line in self:
            line.amount = 0.0
            if (not line.sale_line.product_id.commission_free and
                    line.commission):
                if line.commission.amount_base_type == 'net_amount':
                    subtotal = (line.sale_line.price_subtotal -
                                (line.sale_line.product_id.standard_price *
                                 line.sale_line.product_uom_qty))
                else:
                    subtotal = line.sale_line.price_subtotal
                if line.commission.commission_type == 'fixed':
                    line.amount = subtotal * (line.commission.fix_qty / 100.0)
                else:
                    line.amount = line.commission.calculate_section(subtotal)
