# -*- coding: utf-8 -*-
{
    'name': "Food Consultation",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "FinnD Nguyen",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu_views.xml',
        'views/food_consultation_detail_views.xml',
        'views/food_consultation_detail_button.xml',
        'views/vietnam_food_views.xml',
        # 'views/template.xml',
    ],

    # 'assets': {
    #     'web.assets_backend': ["/ev_food_consultation_web/static/src/js/tree_view_button.js",
    #                            "/ev_food_consultation_web/static/src/xml/tree_view_button.xml"]
    # },

    'application': True,
    'sequence': 2
}
