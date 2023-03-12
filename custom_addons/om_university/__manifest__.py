
{
    'name': 'University Management ',
    'version': '1.0.0',
    'category': 'University',
    'author' : 'Dias Karibaev',
    'sequence': -100,
    'summary': 'University Management System',
    'description': """ This is university management system """,
    'depends': [  ],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/organization_view.xml',
        'views/student_view.xml',
        'views/speciality_view.xml',

    ],
    'demo': [],
    'assets': { },
    'post_init_hook': '',
    'License': 'LGPL-3',
    'auto_install': False,
}
