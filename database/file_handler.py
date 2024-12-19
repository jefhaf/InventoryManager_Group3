import json
import sys

sys.path.append("..")
from inventory.products.product import Product


# region Filehandler
class FileHandler:
    @staticmethod
    def save_to_json(products):
        # products_dicts = [product.to_dict() for product in products]
        with open("database/products.json", "w") as file:
            json.dump(products, file, indent=4)

    @staticmethod
    def load_from_json():
        print(sys.path[0])
        try:
            with open("database/products.json", "r") as file:
                product_dicts = json.load(file)
        except (FileNotFoundError, ImportError):
            return []
        return product_dicts

    @staticmethod
    def save_users_to_json(users):
        users_dicts = [user.to_dict() for user in users]
        with open("users.json", "w") as file:
            json.dump(users_dicts, file, indent=4)

    @staticmethod
    def load_users_from_json():
        user_dicts = {}
        try:
            with open("users.json", "r") as file:
                user_dicts = json.load(file)
        except (FileNotFoundError, ImportError):
            return {}
        return user_dicts


# endregion
