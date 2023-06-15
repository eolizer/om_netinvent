# -*- coding: utf-8 -*-
{
    'name': "Network Inventory",
    'summary': "Network Inventory Management",
    'description': "Network Inventory Management",
    'author': "Yevhen Olkhovyk eolizer@gmail.com",
    'category': 'Generic Modules',
    'version': '15.0.1.0',
    'license': 'LGPL-3',
    'category': 'Inventory',

    # any module necessary for this one to work correctly
    'depends': ['hr', 'cm_tro_personnel'],

    # always loaded
    'data': [

        # Security
        'security/ir.model.access.csv',

        # Views
        'views/ni_networks_views.xml',
        'views/ni_settings_views.xml',
        'views/ni_device_register_views.xml',
        'views/ni_devices_views.xml',
        'views/ni_dev_maintenance.xml',
        'views/ni_dev_interfaces.xml',
        'views/ni_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],

    'assets': {
        'web.assets_backend': [
            'om_netinvent/static/src/scss/style.scss',
        ]

    },

    'installable': True,
    'application': True,
    'auto_install': False,
}
