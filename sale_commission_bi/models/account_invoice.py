# -*- coding: utf-8 -*-

from odoo import api, fields, models


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    @api.depends('invoice_line_ids.agents')
    def _compute_sale_agent(self):
        # Set agent_id on document header if there is only 1 agent in the document
        for record in self:
            sale_agent_id = None
            for line in record.invoice_line_ids:
                for agent in line.agents:
                    if not sale_agent_id:
                        sale_agent_id = agent.agent
                    elif sale_agent_id != agent.agent:
                        sale_agent_id = False
                        break
                if sale_agent_id is False:
                    break
            if sale_agent_id is not None:
                record.sale_agent_id = sale_agent_id

    sale_agent_id = fields.Many2one(
        comodel_name="res.partner",
        string="Sale Agent",
        compute="_compute_sale_agent",
        store=True, readonly=True)

