# -*- coding: utf-8 -*-
# Copyright 2019 Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'sale_agent_profile',
    'summary': 'Set default agent authorization user profile',
    'version': '10.0.0.1.1',
    'category': 'Sales Management',
    'author': 'SHS-AV s.r.l.',
    'website': 'https://www.zeroincombenze.it/',
    'depends': [
        'product',
        'purchase',
        'sale_commission',
        'sales_team',
        'stock',
    ],
    'data': [
        'data/security_access_rules.xml',
        'views/res_partner_view.xml',
        'views/sale_order_view.xml',
        'views/account_invoice_view.xml',
        'views/product_template_view.xml',
        'wizard/wizard_default_agent_user_profile_view.xml',
    ],
    'installable': True,
    'post_init_hook': 'update_link_agents',
}
