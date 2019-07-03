# -*- coding: utf-8 -*-
# Copyright 2019 Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import random
import string
from odoo import models


class ResPartner(models.Model):
    _inherit = "res.partner"

    # user_id = fields.Many2one(
    #     string="User ID", comodel_name="res.users")

    def create_user(self):
        """Create user from current agent partner"""

        def login_from_name(name):
            login = ''
            for ch in name:
                if ((ch >= 'A' and ch <= 'Z') or
                        (ch >= 'a' and ch <= 'z') or
                        (ch >= '0' and ch <= '9') or
                        (ch in ('_', '.'))):
                    login += ch
            return login

        def rand_pwd():
            return ''.join(random.choice(
                string.ascii_uppercase + string.digits) for _ in range(8))

        partner_model = self.env['res.partner']
        user_model = self.env['res.users']
        groups, companies = user_model.default_user_profile()
        for agent in self:
            if (agent.agent and not agent.user_id):
                login = agent.email or login_from_name(agent.name)
                pwd = rand_pwd()
                vals = {
                    'partner_id': agent.id,
                    'login': login,
                    'new_password': pwd,
                    'signature': 'Initial password is %s' % pwd,
                    'company_id': self.env.user.company_id.id,
                    'company_ids': companies,
                    'groups_id': groups,
                }
                user = user_model.create(vals)
                agent.write({'user_id': user.id})
