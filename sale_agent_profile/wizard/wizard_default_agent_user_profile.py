# -*- coding: utf-8 -*-
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
#
from odoo import api, fields, models
from odoo.tools.translate import _
from odoo.exceptions import UserError


class WizardDefaultAgentUserProfile(models.TransientModel):
    _name = "wizard.default.agent.user.profile"
    _description = "Set default agent authorization user profile"


    @api.multi
    def action_set_agent_user_groups(self):
        self.ensure_one()
        users = self.env[self.env.context['active_model']].browse(
            self.env.context['active_ids'])
        users.action_set_agent_user_groups()

        return True
