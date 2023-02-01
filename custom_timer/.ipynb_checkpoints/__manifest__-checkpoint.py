# -*- coding: utf-8 -*-

{
    'name': 'Custom Timer',

    'summary': """This is a timer module""",

    'description': """
        This is a timer module in Odoo 15
    """,

    'author': 'Odooers',

    'website': 'https://www.odoo.com',

    'category': 'Timer',

    'version': '0.01',

    'depends': ['base','helpdesk','contacts'],

    'data': [
        "security/ir.model.access.csv",
        "security/timer_security.xml",
        "views/helpdesk_inherit.xml",
        "views/helpdesk_report_inherit.xml",
        "views/res_alias.xml",
        "views/clasificacion_ticket.xml",
        "views/subclasificacion_ticket.xml",
        "views/res_canales.xml",
        "views/res_partner_inherit.xml",
        "views/res_user_inherit.xml",
    ],

    'demo': [
    ],
}