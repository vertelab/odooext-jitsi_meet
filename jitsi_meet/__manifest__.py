# -*- coding: utf-8 -*-
# © 2020     Sinerkia iD (<https://www.sinerkia.com>).
{
    'name': 'Jitsi Meet Integration',
    'version': '13.0.1.0.0',
    'category': 'Extra Tools',
    'sequence': 1,
    'summary': 'Create and share Jitsi Meet video conferences with other users and external partners',
    'description': """
		Adds a new APP to create and share Jisti Meet video conference meetings between Odoo users. You can invite external users by sending mail from Odoo.
		When you join the meeting Odoo opens a new browser tab so you can keep working on Odoo, and share screen with your partners at Jisti Meet. 
    """,
    "author": "xxxxxxxx",
    "website": "https://xxxxxxxxxx.com",
    "depends": ['base','web','mail'],
    "data": [
        'views/jitsi_meet_views.xml','data/jitsi_meet.xml','data/mail_template.xml','security/ir.model.access.csv','security/base_security.xml',
    ],
    'images': ['images/main_screenshot.png'],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'AGPL-3',
}
