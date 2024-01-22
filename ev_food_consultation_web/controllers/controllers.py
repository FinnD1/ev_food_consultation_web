from odoo import http
import json
from odoo.http import request


class OpenAcademy(http.Controller):
    @http.route("/food", auth="public", website=True)
    def my_template(self, **kw):
        # courses = request.env['food.consultation.detail'].sudo().search([])
        return http.request.render("ev_food_consultation_web.website_sale_image_viewer", {})

    # @http.route("/food", auth='public')
    # def my_template_json(self):
    #     records = request.env['food.consultation.detail'].sudo().search([])
    #     data = {
    #         'records': [{
    #             'name': record.name,
    #             # 'food_template_image_ids': record.food_template_image_ids,
    #         } for record in records]
    #     }
    #     return http.request.make_response(
    #         json.dumps(data)
    #     )