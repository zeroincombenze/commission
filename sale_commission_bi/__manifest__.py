# -*- coding: utf-8 -*-
{
    "name": "Sale Commission BI",
    "version": "10.0.0.1.0",
    "summary": "Add commission values in invoice BI",
    "author": "SHS-AV s.r.l.",
    "website": "https://www.zeroincombenze.it/crm",
    "development_status": "Beta",
    "license": "LGPL-3",
    "depends": ["account", "sale_commission"],
    "data": [
        "views/account_invoice_view.xml",
    ],
    "maintainer": "Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>",
    "installable": True,
    "post_init_hook": "set_agent_id",
}
