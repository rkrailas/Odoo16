from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError

class ProductProduct(models.Model):
    _inherit = "product.product"

    def unlink(self):
        for product in self:
            if product.list_price > 50:
                raise UserError(_('You are not allowed to delete a product having sales price above 50.'))
        return super(ProductProduct, self).unlink()