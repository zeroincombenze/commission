# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError
import odoo.addons.decimal_precision as dp


class SettlementLine(models.Model):
    _inherit = "sale.commission.settlement.line"

    customer = fields.Many2one(related="invoice.partner_id",
                               readonly=True, copy=False, store=True)
    inv_line_quantity = fields.Float(
        related="agent_line.object_id.quantity",
        readonly=True, copy=False, store=True,
        digits=dp.get_precision('Product Unit of Measure'))
    inv_line_currency_id = fields.Many2one(
        related="agent_line.object_id.currency_id",
        readonly=True, copy=False, store=True)
    inv_line_price_unit = fields.Float(
        related="agent_line.object_id.price_unit",
        readonly=True, copy=False, store=True,
        digits=dp.get_precision('Product Price'))
    inv_line_discount = fields.Float(
        related="agent_line.object_id.discount",
        readonly=True, store=True,
        digits=dp.get_precision('Discount'))

    @api.constrains('company_id', 'agent_line')
    def _check_company(self):
        for record in self:
            if record.agent_line.company_id != record.company_id:
                raise UserError(_(
                    'Company must be the same'
                ))
