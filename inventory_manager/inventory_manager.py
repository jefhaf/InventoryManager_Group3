from inventory import products
from database import file_handler


class InventoryManager:
    def __init__(self):
        self.product_database = load_from_json()

    def search_product(self):
        """Search for product in inventory"""
        pass

    def add_product(self):
        """add new product to inventory"""
        pass

    def remove_product(self):
        """Remove existing product from inventory"""
        pass

    def update_quantity(self):
        """Update quantity of a product in inventory"""
        pass

    def get_total_inventory_value(self):
        """Calculate total value of the entire inventory"""
        pass


im = InventoryManager()

print(im.product_database)
