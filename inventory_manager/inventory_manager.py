import sys

sys.path.append("..")
# from inventory.products.product import Product
from inventory.products.electronics import Electronics
from inventory.products.food import Food
from inventory.products.apparel import Apparel
from inventory.products.household import Household
from inventory.products.toys import Toys
from inventory.products.book import Book
from inventory import products
from database import FileHandler


class InventoryManager:
    def __init__(self):
        # Use method to load the database and store in attribute self.product_database
        self.product_database = FileHandler.load_from_json()

    def search_product(self):
        """Search for product in inventory"""
        pass

    def add_product(self):
        """add new product to inventory"""
        print("Please give details about new product:")
        name = input("name: ")
        model = input("Model: ")
        category = input(
            "Category (electronics, food, apparel, household, toys, books): "
        )
        quantity = int(input("Quantity: "))
        price = float(input("Price: "))
        colour = input("Colour: ")

        kwargs = {
            "name": name,
            "model": model,
            "category": category,
            "quantity": quantity,
            "price": price,
            "colour": colour,
        }

        new_product = product_factory(**kwargs)

        new_product_info = new_product.to_dict()

        for item in self.product_database:
            if item["table_name"] == category:
                item["records"].append(new_product_info)

        """ if category.lower() == "electronics":
            new_product = Electronics(name=name, model=model, warranty_years=warranty_years, quantity=quantity, price=price, colour=colour)
            new_product_info = new_product.to_dict()
            for item in self.product_database:
                if item["table_name"] == "electronics":
                    item["records"].append(new_product_info) """

        FileHandler.save_to_json(self.product_database)

    def remove_product(self):
        """Remove existing product from inventory"""
        pass

    def update_quantity(self):
        """Update quantity of a product in inventory"""
        pass

    def get_total_inventory_value(self):
        """Calculate total value of the entire inventory"""
        pass


def product_factory(**kwargs):
    """Factory method to create
    product objects based on category"""

    category = kwargs["category"]

    del kwargs["category"]

    try:
        if category.lower() == "electronics":

            warranty_years = input("Warranty in years: ")

            kwargs["warranty_years"] = warranty_years

            return Electronics(**kwargs)

        elif category.lower() == "food":

            expiration_date = input("Expiration date")

            kwargs["expiration_date"] = expiration_date

            return Food(**kwargs)

        elif category.lower() == "apparel":

            return Apparel(**kwargs)

        elif category.lower() == "household":

            return Household(**kwargs)

        elif category.lower() == "toys":

            return Toys(**kwargs)

        elif category.lower() == "book":

            author = input("Author: ")

            kwargs["author"] = author

            return Book(**kwargs)

        else:

            raise ValueError("Invalid category")

    except ValueError as e:

        print(f"Error:{e}")

        return None


def im_test():
    # Create insctance of InventoryManager
    im = InventoryManager()

    print(im.product_database)

    im.add_product()
    print()

    print(im.product_database)


im_test()
