from odoo import api, fields, models
from odoo.tools.translate import _
from odoo.exceptions import ValidationError, UserError


class FoodConsultationMenu(models.Model):
    _name = 'food.consultation.menu'
    _description = 'Food Consultation Menu'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'name desc'
    _rec_name = 'name'

    name = fields.Char(string='Name', required=True, copy=False, tracking=True, help="Name")
    description = fields.Text(string='Description', tracking=True, help="Description")
    date = fields.Date(string='Date', default=fields.Date.context_today, tracking=True,
                       help="date")
    line_id = fields.Many2many('food.consultation.detail',
                               string='Food deatail',
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
