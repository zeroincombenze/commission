# -*- coding: utf-8 -*-
#
from odoo import api, SUPERUSER_ID


def set_agent_id_default(cr):
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        AccountInvoce = env["account.invoice"]
        for invoice in AccountInvoce.search([]):
            invoice._compute_sale_agent()
        SaleOrder = env["sale.order"]
        for order in SaleOrder.search([]):
            order._compute_sale_agent()


def set_agent_id(cr, registry):
    set_agent_id_default(cr)
