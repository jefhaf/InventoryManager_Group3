import json
from pathlib import Path
import os
import sys
from product_category_factory import ProductCategoryFactory

sys.path.append(str(Path(__file__).parent.parent))
from inventory.products.product import Product

# region mocking data
test_data = [
    {
        "table_name": "electronics",
        "records": [
            {
                "make": "Samsung",
                "model": "Galaxy S23",
                "category": "Electronics",
                "quantity": 25,
                "color": "Black",
                "price": 750.00,
                "unique_id": "EL001",
            },
            {
                "make": "Apple",
                "model": 'MacBook Pro 14"',
                "category": "Electronics",
                "quantity": 15,
                "color": "Silver",
                "price": 1890.00,
                "unique_id": "EL002",
            },
        ],
    }
]
# endregion


# region custom class handler
class ProductEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Product):
            return obj.__dict__
        else:
            # call base class implementation which takes are of
            # raising exceptions for unsupported types
            return json.JSONEncoder.default(self, obj)


# endregion


def save_to_json(target_path, target_file, data):
    # get the current path of the file, regardless of where it is executed from
    current_path = Path.cwd()
    # go to the parent folder
    current_path = current_path.parent
    information_to_safe = []
    for entry in data:
        information_to_safe.append(ProductCategoryFactory.get_category_table(entry))
    # confirm target_path is valid and equal to current path
    if current_path == Path(target_path):
        with open(f"{current_path}/{target_file}", "w") as file:
            json.dump(information_to_safe, file, indent=4)


def load_from_json():
    target_file = "products.json"
    # get the current path of the file, regardless of where it is executed from
    current_path = Path.cwd()
    # check if the file exists beforehand otherwise an error will occur
    if os.path.exists(f"{current_path}/{target_file}"):
        with open(f"{current_path}/{target_file}", "r") as file:
            data = json.load(file)
    else:
        print(f"File {target_file} does not exist")
    return data


# only run if file_handler is run directly
if __name__ == "__main__":

    # save and load the data
    save_to_json("database", "products.json", test_data)
    print(load_from_json())
