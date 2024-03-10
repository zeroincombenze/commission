# -*- coding: utf-8 -*-
{
    "name": "Sales commissions plus",
    "version": "10.0.1.0.0",
    "category": "Sales Management",
    "summary": "Add agent on document header",
    "author": "SHS-AV s.r.l.",
    "website": "https://www.zeroincombenze.it/crm",
    "development_status": "Beta",
    "license": "AGPL-3",
    "depends": ["sale_commission"],
    "data": [
        "views/account_invoice_view.xml",
    ],
    "maintainer": "Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>",
    "installable": True,
    "post_init_hook": "set_agent_id",
}
