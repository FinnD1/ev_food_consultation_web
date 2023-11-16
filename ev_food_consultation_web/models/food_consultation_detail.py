from odoo import api, fields, models
import random

from odoo.tools.translate import _
from odoo.exceptions import ValidationError, UserError


class FoodConsultationDetail(models.Model):
    _name = 'food.consultation.detail'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Collection of Food Detail'
    _order = 'name desc'
    _rec_name = 'name'

    # def _default_request_user_id(self):
    #     current_user = self.env.user
    #     if current_user:
    #         return current_user.name

    name = fields.Char(string='Name', required=True, copy=False, tracking=True, help="Name")
    create_user_id = fields.Many2one('res.users', string='Create User', ondelete='cascade',
                                     help="Create_user_id", tracking=True)
    # create_employee_id = fields.Many2one('hr.employee', string='Create User', ondelete='cascade',
    #                                      default=lambda self: self._default_request_user_id(),
    #                                      help="Create_employee_id", tracking=True)
    image = fields.Image(string="Image")
    description = fields.Char()
    ingredient_ids = fields.One2many('food.consultation.ingredient', 'food_detail_id',
                                     string='Ingredient', help='ingredient_ids', tracking=True,
                                     ondelete='restrict')
    preparation_ids = fields.One2many('food.consultation.preparation', 'food_detail_id',
                                      string='Preparation', help='preparation_ids', tracking=True,
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

    # Writing function Sequence for fields name
    @api.model
    def create(self, vals):
        new_record = super(FoodConsultationDetail, self).create(vals)
        return new_record

    def write(self, vals):
        res = super(FoodConsultationDetail, self).write(vals)
        return res

    def copy(self):
        raise UserError(_("It not possible to dupplicate the record."))

    def action_random_food(self):
        # res = {}
        records = self.env['food.consultation.detail'].search([])
        print(records)
        random_record = random.choice(records)
        # random_record = random.sample(records, 1)
        random_name = random_record.name
        print(random_name)
        # res['warning'] = {'title': _('UserError'),
        #                   'message': _("Món ăn hôm nay của bạn sẽ là: {name}".format(name=random_name))
        #                   }
        # raise res
        raise ValidationError(_("Món ăn hôm nay của bạn sẽ là: {name}".format(name=random_name)))
