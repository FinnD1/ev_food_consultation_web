from odoo import api, fields, models


# Cac buoc can chuan bi
class FoodConsultationPreparation(models.Model):
    _name = 'food.consultation.preparation'
    _description = 'Food Consultation Preparation'

    name = fields.Char(string='Name', required=True, copy=False, help="Name")
    preparation_description = fields.Text(string='Preparation Description', required=True, help='preparation_description')
    food_detail_id = fields.Many2one('food.consultation.detail',
                                     string='Food Detail', ondelete='cascade',
                                     help='food_detail_id')

    # _sql_constraints = [
    #     ('name_unique',
    #      'UNIQUE(name)',
    #      "The name must be UNIQUE")
    # ]
