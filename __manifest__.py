# -*- coding: utf-8 -*-
{
    'name': "Detalles en factura Argentina",

    'summary': """
        Detalles sobre moneda y sobre valor en letras""",

    'description': """
        Detalles sobre moneda y sobre valor en letras
    """,

    'author': "TRIXServer.com",
    'website': "https://TRIXServer.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base', 
        'l10n_ar',
        'account',
    ],

    # always loaded
    'data': [
        'views/templates.xml',
    ],

    'installable' : True,
}
