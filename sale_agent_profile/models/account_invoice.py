# -*- coding: utf-8 -*-

from odoo import api, fields, models


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    agents = fields.Many2many(
        comodel_name="res.partner",
        relation="account_invoice_agent_profile_rel")

    @api.multi
    def _get_invoice_agents(self):
        vals = {}
        for invoice in self:
            agents = []
            for line in invoice.invoice_line_ids:
                if not line.agents:
                    continue
                for agent_info in line.agents:
                    if not agent_info.agent:
                        continue
                    agents.append(agent_info.agent.id)
            vals[invoice.id] = {'agents': [(6, 0, agents)]}
        return vals

    @api.multi
    def write(self, vals):
        res = super(AccountInvoice, self).write(vals)
        vals = self._get_invoice_agents()
        for id in vals:
            super(AccountInvoice, self).write(vals[id])
        return res

    @api.model
    def create(self, vals):
        res = super(AccountInvoice, self).create(vals)
        vals = res._get_invoice_agents()
        for id in vals:
            super(AccountInvoice, self).write(vals[id])
        return res