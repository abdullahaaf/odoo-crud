# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class MaterialType(models.Model):
    _name = 'material.type'
    _description = 'Type of material'

    name = fields.Char('Type', required=True)


class Supplier(models.Model):
    _name = 'material.supplier'
    _description = 'Supplier'

    name = fields.Char('Name', required=True)
    address = fields.Char('Address')
    contact = fields.Char('Contact')


class Material(models.Model):
    _name = 'material.material'
    _description = 'Material'

    code = fields.Char('Code', required=True)
    name = fields.Char('Name', required=True)
    type_id = fields.Many2one('material.type', 'Type', required=True)
    buy_price = fields.Float('Buy Price', required=True)
    supplier_id = fields.Many2one('material.supplier', 'Supplier', required=True)

    @api.constrains('buy_price')
    def _check_buy_price(self):
        for record in self:
            if record.buy_price < 100:
                raise ValidationError("Buy price cannot less than 100!")