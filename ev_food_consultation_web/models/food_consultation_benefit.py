from odoo import api, fields, models
from odoo.tools.translate import _
from odoo.exceptions import ValidationError, UserError


class FoodConsultationBenefit(models.Model):
    _name = 'food.consultation.benefit'
    _description = 'Food Consultation Benefit'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'name desc'
    _rec_name = 'name'

    name = fields.Char(string='Name', required=True, copy=False, tracking=True, help="Name")
    description = fields.Text(string='Description', tracking=True, help="Description")

    # Writing function Sequence for fields name
    @api.model
    def create(self, vals):
        new_record = super(FoodConsultationBenefit, self).create(vals)
        return new_record

    def write(self, vals):
        res = super(FoodConsultationBenefit, self).write(vals)
        return res

    def copy(self):
        raise UserError(_("It not possible to dupplicate the record."))
