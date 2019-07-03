# -*- coding: utf-8 -*-

from openerp import api, SUPERUSER_ID


def update_link_agents(cr, registry):
    """Set agents field in header of sale orders and account invoices"""
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        sale_order_model = env['sale.order']
        sale_order_line_model = env['sale.order.line']
        account_invoice_model = env['account.invoice']
        account_invoice_line_model = env['account.invoice.line']
        orders = []
        for line in sale_order_line_model.search([('agents', '!=', False)]):
            if (line.order_id.id not in orders and
                    not line.order_id.agents):
                orders.append(line.order_id.id)
        invoices = []
        for line in account_invoice_line_model.search(
                [('agents', '!=', False)]):
            if (line.invoice_id.id not in invoices and
                    not line.invoice_id.agents):
                invoices.append(line.invoice_id.id)
        for order_id in orders:
            # print order_id
            order = sale_order_model.browse(order_id)
            vals = order._get_order_agents()
            for id in vals:
                order.write(vals[id])
        for invoice_id in invoices:
            invoice = account_invoice_model.browse(invoice_id)
            vals = invoice._get_invoice_agents()
            for id in vals:
                invoice.write(vals[id])
    return True
