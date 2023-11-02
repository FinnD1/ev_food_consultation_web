from odoo import api, fields, models
import random

from odoo.tools.translate import _
from odoo.exceptions import ValidationError, UserError


class FoodDetail(models.Model):
    _name = 'food.consultation.detail'
    # _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Collection of Food Detail'
    _order = 'name desc'
    _rec_name = 'name'

    def _default_request_user_id(self):
        return self.env.user.employee_id.id if self.env.user.employee_id.id else False

    name = fields.Char(string='Name', required=True, copy=False, tracking=True, help="Name")
    create_employee_id = fields.Many2one('hr.employee', string='Create User', ondelete='cascade',
                                         default=lambda self: self._default_request_user_id(),
                                         help="Create_employee_id", tracking=True)
    image = fields.Image(string="Image")
    description = fields.Char()
    ingredient_ids = fields.One2many('food.consultation.ingredient', 'food_detail_id',
                                     string='Ingredient', help='ingredient_ids', tracking=True,
                                     ondelete='restrict')
    time = fields.Float()
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Favorite'),
    ], default='0', string="Favorite")
    level_difficult = fields.Selection([('easy', 'Easy'),
                                        ('medium', 'Medium'),
                                        ('hard', 'Hard')], string='Level Difficult', defalt='easy')
    rate = fields.Selection([('0', '0 Star'),
                             ('1', '1 Star'),
                             ('2', '2 Star'),
                             ('3', '3 Star'),
                             ('4', '4 Star'),
                             ('5', '5 Star')], string='Rate', defalt='1')

    _sql_constraints = [
        ('name_unique',
         'UNIQUE(name)',
         "The name must be UNIQUE")
    ]

    def action_random_food(self):
        res = {}
        records = self.env['food.consultation.detail'].search([])
        print(records)
        random_record = random.choice(records)
        # random_record = random.sample(records, 1)
        random_name = random_record.name
        print(random_name)
        # res = random.sample(records, 1)
        # return random_name
        res['warning'] = {'title': _('UserError'),
                          'message': _("Món ăn hôm nay của bạn sẽ là: {name}".format(name=random_name))
                          }
        return res
        # if random_name:
        #     return UserError("Món ăn hôm nay của bạn sẽ là: {name}".format(name=random_name))
