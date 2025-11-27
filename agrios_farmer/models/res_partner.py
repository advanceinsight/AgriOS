# Copyright 2025 Advance Insight
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class ResPartner(models.Model):
    _name = "res.partner"
    _inherit = ["res.partner", "agrios.area.mixin"]
    _rec_names_search = [
        "complete_name",
        "email",
        "ref",
        "vat",
        "company_registry",
        "phone",
        "farmer_ref",
    ]

    # Basic farmer details
    farmer_stage = fields.Selection(
        [("draft", "Draft"), ("verified", "Verified")],
        default="draft",
        copy=False,
    )

    is_farmer = fields.Boolean("Farmer", default=False)
    farmer_ref = fields.Char("Farmer Reference", default="/", readonly=True, copy=False)
    farmer_group_id = fields.Many2one(
        comodel_name="farmer.group",
        ondelete="restrict",
        tracking=True,
    )
    highest_education_id = fields.Many2one(
        comodel_name="partner.education",
        ondelete="restrict",
        tracking=True,
    )
    interactions_count = fields.Integer(
        compute="_compute_interactions_count", string="Interactions"
    )
    managed_area_ids = fields.One2many(
        comodel_name="agrios.area",
        inverse_name="manager_id",
        string="Managed Areas",
        readonly=True,
        copy=False,
    )
    responsible_farmer_ids = fields.Many2many(
        comodel_name="res.partner",
        string="Farmers Responsible",
        compute="_compute_responsible_farmer_ids",
    )
    # extra farmer info
    family_size = fields.Integer()
    next_of_kin = fields.Char()
    nok_id = fields.Char(string="NOK ID")
    nok_phone = fields.Char(string="NOK Phone")

    @api.depends("farmer_ref")
    def _compute_display_name(self):
        ret = super()._compute_display_name()
        for partner in self:
            if partner.farmer_ref and partner.farmer_ref != "/":
                partner.display_name = (
                    f"[{partner.farmer_ref}] {partner.display_name or ''}"
                )
        return ret

    def _compute_interactions_count(self):
        for partner in self:
            partner.interactions_count = self.env["farmer.interaction"].search_count(
                [("farmer_id", "=", partner.id)]
            )

    def _compute_responsible_farmer_ids(self):
        """Partner is responsible for the members of the farmer groups in her area."""
        for this in self:
            farmer_groups = this.managed_area_ids.farmer_group_ids
            this.responsible_farmer_ids = farmer_groups.member_ids

    def action_verify_farmer(self):
        for farmer in self:
            vals = farmer._prepare_verify_farmer_vals()
            farmer.with_context(mail_notrack=True).write(vals)

    def _prepare_verify_farmer_vals(self):
        self.ensure_one()
        vals = {"farmer_stage": "verified"}
        if not self.farmer_ref or self.farmer_ref == "/":
            vals["farmer_ref"] = self.env["ir.sequence"].next_by_code("farmer")
        return vals

    def action_view_interactions(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": "Interactions",
            "res_model": "farmer.interaction",
            "view_mode": "list,form",
            "domain": [("farmer_id", "=", self.id)],
            "context": {"default_farmer_id": self.id},
        }

    @api.model
    def web_search_read(
        self, domain, specification, offset=0, limit=None, order=None, count_limit=None
    ):
        # RP: Is usefull at all (is not everybody using mobile in Africa),
        #     this should really go into a separate module in partner-contact.
        if self._context.get("filter_duplicate_phone"):
            self._cr.execute("""
                SELECT DISTINCT ptn1.id
                FROM res_partner ptn1
                INNER JOIN res_partner ptn2 ON ptn1.id != ptn2.id
                AND ptn1.phone = ptn2.phone
                WHERE ptn1.phone IS NOT NULL
            """)
            phone_duplicate_ids = [ptn[0] for ptn in self._cr.fetchall()]
            if domain:
                domain = ["&", ("id", "in", phone_duplicate_ids)] + domain
            else:
                domain = [("id", "in", phone_duplicate_ids)]
        return super().web_search_read(
            domain,
            specification,
            offset=offset,
            limit=limit,
            order=order,
            count_limit=count_limit,
        )
