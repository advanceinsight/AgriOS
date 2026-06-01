# Copyright 2025 Advance Insight
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    verified_partner_farmer = fields.Boolean(
        compute="_compute_verified_partner_farmer",
    )
    farmer_requires_contract = fields.Boolean(
        related="partner_id.farmer_requires_contract",
        readonly=True,
        string="Requires Contract",
    )
    partner_open_contract_ids = fields.One2many(
        related="partner_id.open_contract_ids", readonly=True
    )
    partner_open_contract_harvest_ids = fields.One2many(
        related="partner_id.open_contract_harvest_ids", readonly=True
    )
    farmer_contract_id = fields.Many2one(
        "farmer.contract",
        "Farmer Contract",
        domain="[('farmer_id','=',partner_id),('contract_stage','=','open'),('company_id','=',company_id)]",
    )

    @api.depends("partner_id")
    def _compute_verified_partner_farmer(self):
        for so in self:
            so.verified_partner_farmer = (
                so.partner_id.is_farmer and so.partner_id.farmer_stage == "verified"
            )

    @api.onchange("partner_id")
    def _onchange_agrios_contract(self):
        if self.partner_id:
            if (
                self.farmer_contract_id
                and self.farmer_contract_id.farmer_id == self.partner_id
            ):
                return
            company = self.company_id or self.env.company
            if company.allow_operations_out_of_phase:
                contracts = self.partner_open_contract_ids
            else:
                contracts = self.partner_open_contract_harvest_ids
            if len(contracts) == 1:
                self.farmer_contract_id = contracts
            else:
                self.farmer_contract_id = False
        else:
            self.farmer_contract_id = False

    @api.onchange("farmer_contract_id")
    def _onchange_agrios_oa_id(self):
        if self.farmer_contract_id:
            oftake_prd = self.farmer_contract_id.contracted_crop_id
            balance_qty = max(self.farmer_contract_id.balance_qty * -1, 0)
            self.order_line = [
                (5, 0, 0),
                (
                    0,
                    0,
                    {
                        "product_id": oftake_prd.id,
                        "name": oftake_prd.display_name,
                        "product_qty": balance_qty,
                        "product_uom_id": oftake_prd.uom_po_id.id,
                    },
                ),
            ]
            self.currency_id = self.farmer_contract_id.currency_id
