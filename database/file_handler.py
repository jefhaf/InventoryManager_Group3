import json


# region Filehandler
class FileHandler:
    @staticmethod
    def save_to_json(products):
        with open("products.json", "w") as file:
            json.dump(products, file, indent=4)

    @staticmethod
    def load_from_json():
        try:
            with open("products.json", "r") as file:
                product_dicts = json.load(file)
        except (FileNotFoundError, ImportError):
            return []
        return product_dicts

    @staticmethod
    def save_users_to_json(users):
        with open("users.json", "w") as file:
            json.dump(users, file, indent=4)

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
