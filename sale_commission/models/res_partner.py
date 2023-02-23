# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResPartner(models.Model):
    """Add some fields related to commissions"""
    _inherit = "res.partner"

    agents = fields.Many2many(
        comodel_name="res.partner", relation="partner_agent_rel",
        column1="partner_id", column2="agent_id",
        domain="[('agent', '=', True)]")
    # Fields for the partner when it acts as an agent
    agent = fields.Boolean(
        string="Creditor/Agent",
        help="Check this field if the partner is a creditor or an agent.")
    agent_type = fields.Selection(
        selection=[("agent", "Agent"),
                   ("External agent", "External Agent")],
        string="Type", required=True,
        default="agent")
    commission = fields.Many2one(
        string="Commission", comodel_name="sale.commission",
        help="This is the default commission used in the sales where this "
             "agent is assigned. It can be changed on each operation if "
             "needed.")
    settlement = fields.Selection(
        selection=[("monthly", "Monthly"),
                   ("quaterly", "Quarterly"),
                   ("semi", "Semi-annual"),
                   ("annual", "Annual")],
        string="Settlement period", default="monthly", required=True)
    settlements = fields.One2many(
        comodel_name="sale.commission.settlement", inverse_name="agent",
        readonly=True)
    head_agent = fields.Many2one(
        string="Head Agent", comodel_name="res.partner",
        domain=[('agent_type', '=', 'agent')],
        help="Head agent, if exists"
        )
    head_commission = fields.Many2one(
        string="Head Commission", comodel_name="sale.commission",
        help="Default commission assigned to head agent")

    @api.onchange('agent_type')
    def onchange_agent_type(self):
        if self.agent_type == 'agent' and self.agent:
            self.supplier = True
