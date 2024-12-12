import json
from pathlib import Path
import os
import sys

sys.path.append(str(Path(__file__).parent.parent))
from inventory.products import Product


# region Filehandler
class FileHandler:
    @staticmethod
    def save_to_json(products, filename):
        products_dicts = [product.to_dict() for product in products]
        with open(filename, "w") as file:
            json.dump(products_dicts, file, indent=4)

    @staticmethod
    def load_from_json():
        with open("products.json", "r") as file:
            product_dicts = json.load(file)

        return [Product.from_dict(data) for data in product_dicts]


# endregion
