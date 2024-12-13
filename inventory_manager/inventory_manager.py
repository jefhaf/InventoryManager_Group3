import sys
sys.path.append("..")
from inventory.products.product import Product
from inventory import products
from database import FileHandler


class InventoryManager:
    def __init__(self):
        database_filehandler = FileHandler()
        self.product_database = database_filehandler.load_from_json()

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


def im_test():
    im = InventoryManager()

    print(im.product_database)


im_test()