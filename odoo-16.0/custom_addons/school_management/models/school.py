from odoo import models,fields,api
from datetime import date
from dateutil.relativedelta import relativedelta


class School(models.Model):
    _name = 'school.student'

    name = fields.Many2one('res.partner', string='Student')
    class_id = fields.Integer(string='Class')
    division = fields.Char(string='Division')
    float_no = fields.Float(string='Float Number')
    document = fields.Binary()
    true = fields.Boolean()
    image = fields.Image()
    date = fields.Date(string='Date of Birth')
    age = fields.Integer(string='Age',compute='_compute_age')
    yes_no = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No')
    ], string='Yes or No')
    product_id = fields.Many2one('product.product')
    product_ids = fields.Many2many('product.product')
    price = fields.Monetary()
    currency_id = fields.Many2one('res.currency')
    admn_date = fields.Date(default=fields.date.today())
    officer_id = fields.Many2one('res.users',string='Office',default=lambda self:self.env.user)

    @api.depends('date')
    def _compute_age(self):
        self.age = False
        for rec in self:
            rec.age = relativedelta(date.today(),rec.date).years

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        domain = []
        if name:
            domain = ['|', '|', ('name', operator, name), ('phone', operator, name), ('email', operator, name)]
        return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid)
