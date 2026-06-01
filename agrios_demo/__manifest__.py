# Copyright 2025 Advance Insight
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "AgriOS Demo",
    "summary": """Load AgriOS demo""",
    "author": "Advance Insight",
    "website": "https://agrios.org",
    "category": "AgriOS",
    "version": "19.0.1.0.0",
    "license": "AGPL-3",
    "depends": [
        # Odoo Modules
        "hr",
        # Agrios Modules
        "agrios_trade",
        "agrios_training",
        "agrios_theme",
    ],
    "data": [
        "security/ir.model.access.csv",
        "wizards/agrios_demo.xml",
    ],
    "demo": [
        "demo/hr_department_demo.xml",
        "demo/hr_employee_demo.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "agrios_demo/static/src/components/demo_data_widget/*",
        ],
    },
    "post_init_hook": "post_init_hook",
    "application": False,
    "installable": True,
    "auto_install": False,
}
