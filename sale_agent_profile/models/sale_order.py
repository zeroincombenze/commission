# -*- coding: utf-8 -*-

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    agents = fields.Many2many(
        comodel_name="res.partner",
        relation="sale_order_agent_profile_rel")

    @api.multi
    def _get_order_agents(self):
        vals = {}
        for order in self:
            agents = []
            for line in order.order_line:
                if not line.agents:
                    continue
                for agent_info in line.agents:
                    if not agent_info.agent:
                        continue
                    agents.append(agent_info.agent.id)
            vals[order.id] = {'agents': [(6, 0, agents)]}
        return vals

    @api.multi
    def write(self, vals):
        res = super(SaleOrder, self).write(vals)
        vals = self._get_order_agents()
        for id in vals:
            super(SaleOrder, self).write(vals[id])
        return res

    @api.model
    def create(self, vals):
        res = super(SaleOrder, self).create(vals)
        vals = res._get_order_agents()
        for id in vals:
            super(SaleOrder, self).write(vals[id])
        return res