# -*- coding: utf-8 -*-

from odoo import fields, models


class AccountInvoiceReport(models.Model):
    _inherit = "account.invoice.report"

    sale_agent_id = fields.Many2one(
        comodel_name="res.partner",
        string="Sale Agent",
        domain="[('agent', '=', True)]")

    def _select(self):
        return (
            super(AccountInvoiceReport, self)._select()
            + ",sub.sale_agent_id as sale_agent_id"
        )

    def _sub_select(self):
        return (
            super(AccountInvoiceReport, self)._sub_select()
            + ",ai.sale_agent_id as sale_agent_id"
        )

    def _group_by(self):
        return (
            super(AccountInvoiceReport, self)._group_by()
            + ",ai.sale_agent_id"
        )
