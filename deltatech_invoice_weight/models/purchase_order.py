# ©  2015-2019 Deltatech
# See README.rst file on addons root folder for license details

from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    weight_gross = fields.Float("Gross Weight", digits="Stock Weight", help="The gross weight in Kg.")
    weight_net = fields.Float("Net Weight", digits="Stock Weight", help="The net weight in Kg.")

    @api.model
    def create(self, vals_list):
        # Create the purchase orders using the default implementation
        purchase_orders = super().create(vals_list)

        for purchase_order in purchase_orders:
            new_weight = 0.0
            # Extract the products from the order lines
            for line in purchase_order.order_line:
                # Calculate the new weight
                new_weight += line.product_id.weight * line.product_qty
            # Update the weight fields
            purchase_order.weight_net = new_weight

        return purchase_orders
