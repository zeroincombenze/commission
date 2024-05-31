# -*- coding: utf-8 -*-
import logging

from odoo import SUPERUSER_ID, api
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)

THIS_MODULE = "sale_commission"
MODULE_TO_CHECK = "sale_commission_areamanager"


def check_installed_plus(cr):
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        disable_check = env["ir.config_parameter"].search(
            [("key", "=", "disable_module_incompatibility")]
        )
        disable_check = disable_check and eval(disable_check[0].value) or False
        ir_module = env["ir.module.module"]
        if not disable_check and not ir_module.search(
                [("name", "=", MODULE_TO_CHECK),
                 ("state", "=", ("installed", "to upgrade"))]):
            raise UserError(
                "Please, install module '%s' before upgrade module '%s'\n"
                "or set system parameter <disable_module_incompatibility> to True "
                "in order to force this upgrade.\n\n"
                "You are warned this choice might be dangerous!"
                % (MODULE_TO_CHECK, THIS_MODULE))


def migrate(cr, version):
    if not version:
        return
    check_installed_plus(cr)
