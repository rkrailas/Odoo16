# -*- coding: utf-8 -*-
from odoo import fields, models, api, _
from odoo.exceptions import ValidationError
from datetime import date
from dateutil.relativedelta import relativedelta


class ResPartner(models.Model):
    _inherit = 'res.partner'

    dob = fields.Date(string='Date of Birth')
    age = fields.Integer(string='Age',compute='_compute_age')


    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('dob'):
                raise ValidationError(_("DOB fiels can not be emply"))
        res = super(ResPartner, self).create(vals_list)

        return res

    @api.depends('dob')
    def _compute_age(self):
        self.age = False
        for rec in self:
            rec.age = relativedelta(date.today(), rec.dob).years

    @api.constrains('dob')
    def validation_constrains(self):
        today = fields.date.today()
        for rec in self:
            if rec.dob > today:
                raise ValidationError('Invalid Date of Brith')

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        domain = []
        if name:
            domain = ['|', '|', ('name', operator, name), ('phone', operator, name), ('email', operator, name)]
        return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid)
