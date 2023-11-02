from odoo import api, fields, models


class VietNamFood(models.Model):
    _name = 'vietnam.food'

    name = fields.Char(string='Name', required=True, copy=False, tracking=True, help="Name")
