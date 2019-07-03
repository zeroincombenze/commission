# -*- coding: utf-8 -*-
# Copyright 2019 Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class ResUsers(models.Model):
    _inherit = "res.users"

    def default_user_profile(self):
        groups = [
            (6, 0,
             [self.env.ref('sale_agent_profile.group_sale_agent').id,
              self.env.ref('sales_team.group_sale_salesman').id,
              self.env.ref('account.group_account_invoice').id,
              self.env.ref('stock.group_stock_user').id,])]
        companies = [(6, 0, [self.env.user.company_id.id])]
        return groups, companies

    def action_set_agent_user_groups(self):
        """Set default agent authorization user profile"""
        for user in self:
            if not user.partner_id.agent:
                continue
            groups, companies = user.default_user_profile()
            vals = {'company_ids': companies,
                    'groups_id': groups,
            }
            user.write(vals)
