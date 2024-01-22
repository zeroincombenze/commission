# -*- coding: utf-8 -*-

from openerp import api, SUPERUSER_ID


def migrate(cr, version):
    """Set agents field in header of sale orders and account invoices"""
    if not version:
        return
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        account_invoice_model = env['account.invoice']
        # account_invoice_line_model = env['account.invoice.line']
        # agent_line_model = env['account.invoice.line.agent']
        for invoice in account_invoice_model.search(
                [('sale_agent_id', '=', False)]):
            invoice._compute_sale_agent()
            # sale_agent_id = None
            # for line in invoice.invoice_line_ids:
            #     for agent in line.agents:
            #         if not sale_agent_id:
            #             sale_agent_id = agent.agent
            #         elif sale_agent_id != agent.agent:
            #             sale_agent_id = False
            #             break
            #     if sale_agent_id is False:
            #         break
            # if sale_agent_id is not None:
            #     invoice.write({"sale_agent_id": sale_agent_id.id})
