# Copyright 2025 Advance Insight
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "AgriOS Training and Certification",
    "summary": """Manage farmer training and education""",
    "author": "Advance Insight",
    "website": "https://agrios.org",
    "category": "AgriOS",
    "version": "19.0.1.0.1",
    "license": "AGPL-3",
    "depends": [
        # Agrios Modules
        "agrios_farmer",
    ],
    "data": [
        "security/res_groups.xml",
        "security/ir.model.access.csv",
        "security/ir_rule.xml",
        "data/res_partner_category_data.xml",
        "data/certification_type_data.xml",
        "views/certification_type_views.xml",
        "views/farmer_certification_views.xml",
        "views/corrective_action_views.xml",
        "views/farmer_training_views.xml",
        "views/res_partner_views.xml",
        "views/training_topic_views.xml",
        # actions, menu and configuration.
        "views/ir_actions_act_window.xml",
        "views/ir_ui_menu.xml",
        "views/res_config_settings_views.xml",
    ],
    "demo": [
        "demo/training_topic_demo.xml",
        "demo/farmer_certification_demo.xml",
        "demo/res_partner_demo.xml",
    ],
    "application": True,
    "installable": True,
    "auto_install": False,
}
