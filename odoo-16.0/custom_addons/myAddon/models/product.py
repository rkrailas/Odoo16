# 25 Nov 23 ยังไม่ Work
from odoo import models
from odoo.exceptions import UserError

class ProductProductInherit(models.Model):
    _inherit = "product.product"

    def unlink(self):
        for product in self:
            if product.list_price > 10:
                raise UserError('You are not allowed to delete a product')
        return super(ProductProduct, self).unlink()
