from odoo.tests.common import TransactionCase


class TestmaterialModel(TransactionCase):
    def setUp(self):
        super().setUp()
        self.Material = self.env['material.material']
        self.MaterialType = self.env['material.type']
        self.Supplier = self.env['material.supplier']

        # Create test data
        self.material_type = self.MaterialType.create({'name': 'Fabric'})
        self.supplier = self.Supplier.create({'name': 'Supplier 1'})

    def test_create_material(self):
        # Create a new material
        material = self.Material.create({
            'code': 'ITM001',
            'name': 'material 1',
            'type_id': self.material_type.id,
            'buy_price': 150,
            'supplier_id': self.supplier.id,
        })

        # Assert the material is created
        self.assertEqual(material.code, 'ITM001')
        self.assertEqual(material.name, 'material 1')
        self.assertEqual(material.type_id, self.material_type)
        self.assertEqual(material.buy_price, 150)
        self.assertEqual(material.supplier_id, self.supplier)

    def test_update_material(self):
        # Create an material
        material = self.Material.create({
            'code': 'ITM002',
            'name': 'material 2',
            'type_id': self.material_type.id,
            'buy_price': 200,
            'supplier_id': self.supplier.id,
        })

        # Update the material
        material.write({
            'name': 'Updated material',
            'buy_price': 250,
        })

        # Assert the material is updated
        self.assertEqual(material.name, 'Updated material')
        self.assertEqual(material.buy_price, 250)

    def test_delete_material(self):
        # Create an material
        material = self.Material.create({
            'code': 'ITM003',
            'name': 'material 3',
            'type_id': self.material_type.id,
            'buy_price': 300,
            'supplier_id': self.supplier.id,
        })

        # Delete the material
        material.unlink()

        # Assert the material is deleted
        deleted_material = self.Material.search([('id', '=', material.id)])
        self.assertFalse(deleted_material)

    def test_filter_materials_by_type(self):
        # Create multiple materials with different types
        material_type_2 = self.MaterialType.create({'name': 'Jeans'})
        material_type_3 = self.MaterialType.create({'name': 'Cotton'})

        material1 = self.Material.create({
            'code': 'ITM001',
            'name': 'material 1',
            'type_id': self.material_type.id,
            'buy_price': 100,
            'supplier_id': self.supplier.id,
        })

        material2 = self.Material.create({
            'code': 'ITM002',
            'name': 'material 2',
            'type_id': material_type_2.id,
            'buy_price': 200,
            'supplier_id': self.supplier.id,
        })

        material3 = self.Material.create({
            'code': 'ITM003',
            'name': 'material 3',
            'type_id': material_type_3.id,
            'buy_price': 300,
            'supplier_id': self.supplier.id,
        })

        # Filter materials by type
        filtered_materials = self.Material.search([('type_id', '=', self.material_type.id)])

        # Assert the correct materials are filtered
        self.assertEqual(len(filtered_materials), 1)
        self.assertIn(material1, filtered_materials)
        self.assertNotIn(material2, filtered_materials)
        self.assertNotIn(material3, filtered_materials)