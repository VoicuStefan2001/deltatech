# ©  2015-2021 Deltatech
#              Dorin Hongu <dhongu(@)gmail(.)com
# See README.rst file on addons root folder for license details

import json

from odoo import models
from odoo.tools import safe_eval


class AccountInvoice(models.Model):
    _inherit = "account.move"

    def open_payments(self):
        self.ensure_one()
        invoice_payments_widget = json.loads(self.invoice_payments_widget)
        payment_ids = []
        for item in invoice_payments_widget.get("content", []):
            payment_ids.append(item["account_payment_id"])

        if self.type == "out_invoice":
            action_ref = "account.action_account_payments_payable"
        else:
            action_ref = "account.action_account_payments"
        [action] = self.env.ref(action_ref).read()
        action["context"] = dict(safe_eval(action.get("context")))

        if len(payment_ids) > 1:
            action["domain"] = [("id", "in", payment_ids)]
        elif payment_ids:
            action["views"] = [(self.env.ref("account.view_account_payment_form").id, "form")]
            action["res_id"] = payment_ids[0]
        return action
