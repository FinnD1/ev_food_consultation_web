from odoo import api, fields, models
from odoo.tools.translate import _
from odoo.exceptions import ValidationError, UserError


class FoodConsultationDessert(models.Model):
    _name = 'food.consultation.dessert'
    _description = 'Food Consultation Dessert'
    _inherit = ['food.consultation.detail', 'mail.thread', 'mail.activity.mixin']
    _order = 'name desc'
    _rec_name = 'name'

    season_id = fields.Many2one('food.consultation.season', string='Season', help='season_id', tracking=True,
                                ondelete='restrict')
    benefit_id = fields.Many2many('food.consultation.benefit', string='Benefit', help='benefit_id', tracking=True,
                                  ondelete='restrict')
    food_dessert_id = fields.Many2one('food.consultation.menu',
                                     string='Food Menu', ondelete='cascade',
                                     help='food_menu_id')
