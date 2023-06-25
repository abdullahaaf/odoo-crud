# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class ItemController(http.Controller):
    @http.route('/material/create', auth='user', type='json', methods=['POST'])
    def create_material(self, code, name, type_id, buy_price, supplier_id):
        Material = request.env['material.material']
        vals = {
            'code': code,
            'name': name,
            'type_id': type_id,
            'buy_price': buy_price,
            'supplier_id': supplier_id
        }
        material = Material.create(vals)
        return material.read()
    

    @http.route('/material/read', auth='user', type='json', methods=['GET'])
    def read_material(self, material_code):
        Material = request.env['material.material']
        material = Material.browse(material_code)
        return material.read()
    

    @http.route('/maerial/update', auth='user', type='json', methods=['POST'])
    def update_material(self, code, name, type_id, buy_price, supplier_id):
        Material = request.env['material.material']
        material = Material.browse(code)
        vals = {
            'name': name,
            'type_id': type_id,
            'buy_price': buy_price,
            'supplier_id': supplier_id,
        }
        material.write(vals)
        return material.read()
    

    @http.route('/material/delete', auth='user', type='json', methods=['POST'])
    def delete_material(self, code):
        Material = request.env['material.material']
        material = Material.browse(code)
        material.unlink()

    
    @http.route('/material/filter', auth='user', type='json', methods=['GET'])
    def filter_material_by_type(self, type_id):
        Material = request.env['material.material']
        material = Material.search([('type_id', '=', type_id)])
        return material.read(['code', 'name', 'buy_price'])