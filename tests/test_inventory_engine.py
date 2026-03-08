import unittest
from src.inventory_engine import reconcile_inventory


class InventoryCalculationTests(unittest.TestCase):

    def test_inventory_reduction(self):

        inventory = {
            "1": {
                "product_name": "Phone",
                "current_stock": 50,
                "unit_price": 100,
                "category": "Electronics"
            }
        }

        sales = {"1": 10}

        result = reconcile_inventory(inventory, sales)

        self.assertEqual(result[0]["final_stock"], 40)

    def test_inventory_not_negative(self):

        inventory = {
            "1": {
                "product_name": "Phone",
                "current_stock": 5,
                "unit_price": 100,
                "category": "Electronics"
            }
        }

        sales = {"1": 10}

        result = reconcile_inventory(inventory, sales)

        self.assertEqual(result[0]["final_stock"], 0)

    def test_zero_stock_status(self):

        inventory = {
            "1": {
                "product_name": "Phone",
                "current_stock": 10,
                "unit_price": 100,
                "category": "Electronics"
            }
        }

        sales = {"1": 10}

        result = reconcile_inventory(inventory, sales)

        self.assertEqual(result[0]["stock_status"], "OUT_OF_STOCK")

    def test_low_stock_status(self):

        inventory = {
            "1": {
                "product_name": "Phone",
                "current_stock": 10,
                "unit_price": 100,
                "category": "Electronics"
            }
        }

        sales = {"1": 5}

        result = reconcile_inventory(inventory, sales)

        self.assertEqual(result[0]["stock_status"], "LOW_STOCK")

    def test_available_status(self):

        inventory = {
            "1": {
                "product_name": "Phone",
                "current_stock": 50,
                "unit_price": 100,
                "category": "Electronics"
            }
        }

        sales = {"1": 5}

        result = reconcile_inventory(inventory, sales)

        self.assertEqual(result[0]["stock_status"], "AVAILABLE")

    def test_sales_value_calculation(self):

        inventory = {
            "1": {
                "product_name": "Phone",
                "current_stock": 50,
                "unit_price": 100,
                "category": "Electronics"
            }
        }

        sales = {"1": 5}

        result = reconcile_inventory(inventory, sales)

        self.assertEqual(result[0]["total_sales_value"], 500)

    def test_no_sales_case(self):

        inventory = {
            "1": {
                "product_name": "Phone",
                "current_stock": 50,
                "unit_price": 100,
                "category": "Electronics"
            }
        }

        sales = {}

        result = reconcile_inventory(inventory, sales)

        self.assertEqual(result[0]["final_stock"], 50)
