# Copyright 2025 Advance Insight
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
import base64

from odoo import models
from odoo.modules.loading import load_demo
from odoo.modules.module_graph import ModuleGraph
from odoo.tools import file_open

from odoo.addons.base.models.ir_module import assert_log_admin_access


class AgriosDemo(models.TransientModel):
    _name = "agrios.demo"
    _description = "Agrios Demo"

    @assert_log_admin_access
    def action_load_demo_for_agrios(self):
        self.ensure_one()
        env = self.env(su=True)
        currency = env.ref("base.KES")
        currency.write({"active": True})
        env.company.write(
            {
                "name": "AgriGrowth Nairobi",
                "currency_id": currency.id,
                "country_id": env.ref("base.ke").id,
                "logo": self._load_image_base64("demo", "agri-growth-nairobi.png"),
            }
        )

        graph = ModuleGraph(env.cr, mode="load")
        graph.extend(["agrios"])
        node = graph["agrios"]
        node.demo = True
        load_demo(env, node, {}, "init")
        env.clear()
        env["res.partner"].search([("is_farmer", "=", True)]).action_verify_farmer()

        # update Department Manager
        env.ref("agrios.department_admin_finance").write(
            {
                "manager_id": env.ref("agrios.employee_1").id,
            }
        )
        env.ref("agrios.department_field_operations").write(
            {
                "manager_id": env.ref("agrios.employee_2").id,
            }
        )
        env.ref("agrios.department_hr_communication").write(
            {
                "manager_id": env.ref("agrios.employee_2").id,
            }
        )
        env.ref("agrios.department_it").write(
            {
                "manager_id": env.ref("agrios.employee_11").id,
            }
        )
        env.ref("agrios.department_monitoring_evaluation").write(
            {
                "manager_id": env.ref("agrios.employee_12").id,
            }
        )
        env.ref("agrios.department_training").write(
            {
                "manager_id": env.ref("agrios.employee_13").id,
            }
        )

        return {
            "type": "ir.actions.act_url",
            "target": "self",
            "url": "/odoo",
        }

    def _load_image_base64(self, *path_parts):
        """Convert an image file into a base64-encoded string."""
        rel_path = "/".join(("agrios_demo",) + path_parts)
        with file_open(rel_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data)
