# -*- coding: utf-8 -*-

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    # Wil be named to area_manager_id
    head_agent = fields.Many2one(
        string="Head Agent",
        comodel_name="res.partner",
        domain=[('agent_type', '=', 'agent'), ('area_manager', '=', True)],
        help="Head agent, if exists"
        )
    area_manager = fields.Boolean(
        string="Is Area Manager", help="This agent is an area manager")
    area_manager_sub_agent_ids = fields.One2many(
        comodel_name="res.partner", inverse_name="head_agent",
        string="Agents", readonly=True)
    # Will be renamed commission_for_areamanager
    head_commission = fields.Many2one(
        string="Head Commission",
        comodel_name="sale.commission",
        help="Default commission assigned to head agent")
