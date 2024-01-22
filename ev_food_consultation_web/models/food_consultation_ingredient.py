from odoo import api, fields, models

from odoo.tools.translate import _
from odoo.exceptions import ValidationError, UserError


# Nguyên liệu
class FoodConsultationIngredient(models.Model):
    _name = 'food.consultation.ingredient'
    _description = 'Food Consultation Ingredient'

    name = fields.Char(string='Name', required=True, copy=False, help="Name")
    food_detail_id = fields.Many2one('food.consultation.detail',
                                     string='Food Detail', ondelete='cascade',
                                     help='food_detail_id')
    request_qty = fields.Integer(string='Request Quantity', help='request_qty', default=1)
    ingredient_description = fields.Text(string='Ingredient Description', required=True, help='ingredient_description')


    @api.onchange('request_qty')
    def _check_qty(self):
        for res in self:
            if res.request_qty < 0:
                raise UserError(_("Request quantity must be non-negative"))
