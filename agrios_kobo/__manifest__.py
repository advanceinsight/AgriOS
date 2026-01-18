# Copyright 2025 Advance Insight
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Kobo Toolbox Integration - Agrios",
    "summary": """Kobo Toolbox Extention For Agrios Application""",
    "author": "Advance Insight",
    "website": "https://agrios.org",
    "category": "AgriOS",
    "version": "18.0.1.0.5",
    "license": "AGPL-3",
    "depends": [
        "ai_kobo_integration",
        "agrios",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/kobo_asset_actions.xml",
        "views/action_utils_models.xml",
    ],
    "application": False,
    "installable": False,
    "auto_install": False,
}
