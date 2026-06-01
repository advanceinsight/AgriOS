# -*- coding: utf-8 -*-
# Copyright 2025 Advance Insight
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Cloudpepper Connector",
    "summary": "Manage Odoo instances via the Cloudpepper API",
    "author": "Advance Insight",
    "website": "https://www.agrios.org",
    "category": "AgriOS",
    "version": "19.0.1.2.0",
    "license": "AGPL-3",
    "depends": [
        "web",
        "mail",
    ],
    "external_dependencies": {
        "python": ["requests"]
    },
    "data": [
        "security/ir.model.access.csv",
        "data/ir_cron.xml",
        "data/ir_sequence.xml",
        "wizard/setup_wizard_views.xml",
        "wizard/cloudpepper_instance_module_wizard.xml",
        "views/cloudpepper_settings_views.xml",
        "views/cloudpepper_default_module.xml",
        "views/cloudpepper_server_views.xml",
        "views/cloudpepper_instance_views.xml",
        "views/menu.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}