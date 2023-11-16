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
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/food_security.xml',
        'security/ir.model.access.csv',
        'views/menu_views.xml',
        'views/food_consultation_detail_views.xml',
        'views/food_consultation_menu_views.xml',
        # 'views/food_consultation_detail_button.xml',
        # 'views/template.xml',
    ],

    'assets': {
        'web.assets_backend': ["/ev_food_consultation_web/static/src/scss/style.scss",
                               "/ev_food_consultation_web/static/src/css/style.css"]
    },
    # 'assets': {
    #     'web._assets_primary_variables': [
    #         'account/static/src/scss/variables.scss',
    #     ],
    #     'web.assets_backend': [
    #         'account/static/src/css/account_bank_and_cash.css',
    #         'account/static/src/css/account.css',
    #         'account/static/src/scss/account_journal_dashboard.scss',
    #         'account/static/src/scss/account_dashboard.scss',
    #         'account/static/src/scss/account_searchpanel.scss',
    #         'account/static/src/scss/legacy_account_activity.scss',
    #         'account/static/src/js/legacy_account_payment_field.js',
    #         'account/static/src/js/legacy_mail_activity.js',
    #         'account/static/src/js/legacy_tax_totals.js',
    #         'account/static/src/js/legacy_section_and_note_fields_backend.js',
    #         'account/static/src/js/legacy_account_selection.js',
    #         'account/static/src/js/legacy_open_move_widget.js',
    #         'account/static/src/components/**/*',
    #         'account/static/src/js/tours/account.js',
    #         'account/static/src/xml/**/*',
    #     ],
        # 'web.assets_frontend': [
        #     'account/static/src/js/account_portal_sidebar.js',
        #     'account/static/src/js/account_portal.js',
        # ],
        # 'web.assets_tests': [
        #     'account/static/tests/tours/**/*',
        # ],
        # 'web.qunit_suite_tests': [
        #     'account/static/tests/*.js',
        # ],

    # "qweb": ['static/xml/tree_view_button.xml'],

    'application': True,
    'sequence': 2
}
