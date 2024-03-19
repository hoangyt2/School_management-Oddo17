# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Student Management',
    'version': '1.0',
    'summary': 'Student management version 1.0',
    'description': """
    Modules quản lý học sinh
    """,
    'depends': ['class'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_information.xml',
        'views/subject_information.xml'
    ],
    'demo': [],
    'installable': True,
    'license': 'LGPL-3',
}
