# -*- coding: utf-8 -*-

from openerp import api, SUPERUSER_ID


def migrate(cr, version):
    """Set agents field in header of sale orders and account invoices"""
    if not version:
        return
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        account_invoice_model = env['account.invoice']
        # account_invoice_line_model = env['account.invoice.line']
        # agent_line_model = env['account.invoice.line.agent']
        for invoice in account_invoice_model.search(
                [('sale_agent_id', '=', False)]):
            invoice._compute_sale_agent()
