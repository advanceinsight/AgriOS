# Copyright 2025 Advance Insight
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "AgriOS Theme",
    "summary": """Green theme for the Agrios modules""",
    "author": "Advance Insight",
    "website": "https://agrios.org",
    "category": "AgriOS",
    "version": "19.0.1.0.0",
    "license": "AGPL-3",
    "depends": [
        # Odoo Modules
        "web",
    ],
    "assets": {
        "web.assets_backend": [
            "agrios_theme/static/src/module/module_styles.scss",
        ],
        "web._assets_primary_variables": [
            (
                "before",
                "web/static/src/scss/primary_variables.scss",
                "agrios_theme/static/src/scss/primary_variables.scss",
            ),
        ],
    },
    "application": True,
    "installable": True,
    "auto_install": False,
}
