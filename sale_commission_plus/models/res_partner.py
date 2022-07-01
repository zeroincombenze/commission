# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    agent_type = fields.Selection(
        selection_add=[("External agent", "External Agent")],
        string="Type",
        required=True,
        default="agent")
    head_agent = fields.Many2one(
        string="Head Agent",
        comodel_name="res.partner",
        domain=[('agent_type', '=', 'agent')],
        help="Head agent, if exists"
        )
    head_commission = fields.Many2one(
        string="Head Commission",
        comodel_name="sale.commission",
        help="Default commission assigned to head agent")
