# -*- coding: utf-8 -*-

from odoo import fields, models


class AccountInvoiceReport(models.Model):
    _inherit = "account.invoice.report"

    sale_agent = fields.Many2one(
        comodel_name="res.partner",
        string="Sale Agent",
        domain="[('agent', '=', True)]")

    # def _from(self):
    #     return (
    #         super(AccountInvoiceReport, self)._from()
    #         + " LEFT JOIN account_invoice_line_agent la ON la.invoice_line = ail.id"
    #     )
