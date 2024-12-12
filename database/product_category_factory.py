import os
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from inventory.products.product import Product


class ProductCategoryFactory:
    @staticmethod
    def get_category_table(list_of_products: list):
        data = []
        if Product.category == "Electronics":
            for entry in list_of_products:
                if entry.category == "Electronics":
                    data.append(entry)
                    return {"table_name": "electronics", "records": data}
        elif Product.category == "Books":
            for entry in list_of_products:
                if entry.category == "Books":
                    data.append(entry)
                    return {"table_name": "books", "records": data}
        elif Product.category == "Apparel":
            for entry in list_of_products:
                if entry.category == "Apparel":
                    data.append(entry)
                    return {"table_name": "apparel", "records": data}
        elif Product.category == "Household":
            for entry in list_of_products:
                if entry.category == "Household":
                    data.append(entry)
                    return {"table_name": "household", "records": data}
        elif Product.category == "Food":
            for entry in list_of_products:
                if entry.category == "Food":
                    data.append(entry)
                    return {"table_name": "food", "records": data}
        elif Product.category == "Toys":
            for entry in list_of_products:
                if entry.category == "Toys":
                    data.append(entry)
                    return {"table_name": "toys", "records": data}
        else:
            return None

    @staticmethod
    def get_default_category_table():
        return [
            {"table_name": "electronics", "records": []},
            {"table_name": "food", "records": []},
            {"table_name": "apparel", "records": []},
            {"table_name": "household", "records": []},
            {"table_name": "toys", "records": []},
            {"table_name": "books", "records": []},
        ]