# -*- coding: utf-8 -*-
{
    'name': 'School Management',
    'summary': 'School Management Software',
    'sequence': 10,
    'description': """
School Management
====================
The specific and easy-to-use Invoicing system in Odoo allows you to keep track of your accounting, even when you are not an accountant. It provides an easy way to follow up on your vendors and customers.

You could use this simplified accounting in case you work with an (external) account to keep your books, and you still want to keep track of payments. This module also offers you an easy method of registering payments, without having to encode complete abstracts of account.
    """,
    'category': 'Tools',
    'version': '16.0.1.0.0',
    'website': 'https://www.yourwebsite.com/',
    'depends': ['base', 'contacts', 'hr', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/school.xml',
        'report/school_report.xml',
        'report/school_template.xml'
    ],
    'demo': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
