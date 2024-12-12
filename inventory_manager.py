from inventory import *
from database import *


class InventoryManager:
    def __init__(self):
        self.products = load_from_json()

    def search_product(self, query):
        """Search for product in inventory"""
        results = [product.get_product_info() for name, product in self.products.items() if query.lower() in name.lower()]
        return results if results else "Product not found"

    def add_product(self, product):
        """add new product to inventory"""
        if product.name in self.products:
            raise ValueError(f"Product '{product.name}' already exists in inventory")
        self.products[product.name] = product

    def remove_product(self, product_name):
        """Remove existing product from inventory"""
        if product_name in self.products:
            del self.products[product_name]
        else:
            raise ValueError(f"Product '{product_name}' not found in inventory")

    def update_quantity(self, product_name, quantity):
        """Update quantity of a product in inventory"""
        if product_name in self.products:
            self.products[product_name].update_quantity(quantity)
        else:
            raise ValueError(f"Product '{product_name}' not found in inventory")

    def get_total_inventory_value(self):
        """Calculate total value of the entire inventory"""
        return sum(product.price * product.quantity for product in self.products.values())
