import json
import sys

sys.path.append("..")
from inventory.products.product import Product


# region Filehandler
class FileHandler:
    @staticmethod
    def save_to_json(products, filename="database/products.json"):
        # products_dicts = [product.to_dict() for product in products]
        with open(filename, "w") as file:
            json.dump(products, file, indent=4)

    @staticmethod
    def load_from_json(filename="database/products.json"):
        print(sys.path[0])
        try:
            with open(filename, "r") as file:
                product_dicts = json.load(file)
        except (FileNotFoundError, ImportError) as error:
            print(error)
            return []
        return product_dicts

    @staticmethod
    def save_users_to_json(users, filename="users.json"):
        users_dicts = [user.to_dict() for user in users]
        with open(filename, "w") as file:
            json.dump(users_dicts, file, indent=4)

    @staticmethod
    def load_users_from_json(filename="users.json"):
        user_dicts = {}
        try:
            with open(filename, "r") as file:
                user_dicts = json.load(file)
        except (FileNotFoundError, ImportError):
            return {}
        return user_dicts


# endregion
