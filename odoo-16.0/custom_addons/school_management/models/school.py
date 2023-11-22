from odoo import models, fields, api


class School(models.Model):
    _name = 'school.student'

    name = fields.Many2one('res.partner', string='Student')
    class_id = fields.Integer(string='Class')
    division = fields.Char(string='Division')

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        domain = []
        if name:
            domain = ['|', '|', ('name', operator, name), ('phone', operator, name), ('email', operator, name)]
        return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid)
