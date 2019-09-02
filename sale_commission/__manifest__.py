# -*- coding: utf-8 -*-
{
    'name': 'Sales commissions',
    'version': '10.0.11.0.0',
    'category': 'Sales Management',
    'author': 'Odoo Community Association (OCA) and other subjects',
    'license': 'AGPL-3',
    'depends': [
        'account',
        'product',
        'sale',
        'stock_account',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_commission_view.xml',
        'views/product_template_view.xml',
        'views/res_partner_view.xml',
        'views/sale_order_view.xml',
        'views/account_invoice_view.xml',
        'views/settlement_view.xml',
        'wizard/wizard_settle.xml',
        'wizard/wizard_invoice.xml',
        'report/report_sale.xml',
    ],
    'demo': ['demo/sale_agent_demo.xml'],
    'installable': True,
}
