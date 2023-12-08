from odoo import api, fields, models
import random

from odoo.tools.translate import _
from odoo.exceptions import ValidationError, UserError


class FoodConsultationMenu(models.Model):
    _name = 'food.consultation.menu'
    _description = 'Food Consultation Menu'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'name desc'
    _rec_name = 'name'

    name = fields.Char(string='Name', copy=False, tracking=True, help="Name")
    description = fields.Text(string='Description', tracking=True, help="Description")
    date = fields.Date(string='Date', default=fields.Date.context_today, tracking=True,
                       help="date")
    line_id = fields.Many2many('food.consultation.detail','food_menu_id',
                               string='Food deatail',
                               ondelete='cascade')
    line_dessert_id = fields.Many2many('food.consultation.dessert','food_dessert_id',
                               string='Food Dessert',
                               ondelete='cascade')

    # Writing function Sequence for fields name
    @api.model
    def create(self, vals):
        new_record = super(FoodConsultationMenu, self).create(vals)
        new_record.name = self.env['ir.sequence'].next_by_code('food.consultation.menu')
        for line in new_record:
            line.name = new_record.name
        return new_record

    def write(self, vals):
        res = super(FoodConsultationMenu, self).write(vals)
        return res

    def copy(self):
        raise UserError(_("It not possible to dupplicate the record."))

    def action_random_menu(self):
        records = self.env['food.consultation.detail'].search([])
        records_dessert = self.env['food.consultation.dessert'].search([])
        random_records = random.sample(records, 5)
        random_records_dessert = random.sample(records_dessert, 1)

        record_ids = []
        record_dessert_ids = []
        for record in random_records:
            record_ids.append(record.id)

        for res in random_records_dessert:
            record_dessert_ids.append(res.id)

        self.line_dessert_id = [(6, 0, record_dessert_ids)]
        self.line_id = [(6, 0, record_ids)]

    @api.onchange('line_id')
    def _onchange_images(self):
        if self.line_id:
            image_ids = self.line_id.mapped('image_ids.id')
            self.images = [(6, 0, image_ids)]


