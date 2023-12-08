from odoo import api, fields, models
from odoo.tools.translate import _
from odoo.exceptions import ValidationError, UserError


class FoodIntro(models.Model):
    _name = 'food.intro'
    _description = 'Food Intro'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'name desc'
