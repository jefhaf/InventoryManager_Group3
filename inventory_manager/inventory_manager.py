"""Inventory Manager

This module handles all the functions related to searching, adding, removing items inside a database.

This module requires 'stringcolor' to be installed to run properly inside the terminal.

Inside this module are the following classes and methods:
Classes:
    LowPriceException: Custom exception for user inputs that cannot be converted into floats (needed for testing).
    InventoryManager: Class that handles all functionality.
Methods (InventoryManager):
    search_product_by_user: Gets info from user to search for product(s). --> calls search_product()
    search_product: Filters through a database to return items that meet requirements. --> gets called by search_product_by_user()
    is_exist_product: Checks if an item already exists inside the database and returns a boolean value.
    add_product: Adds a product to the database and saves said database after that is done.
    ask_for_confirmation: Asks for validation from the user to remove an item. --> gets called by remove_product()
    remove_product: Asks for Make and Model to find and possibly remove a found item. --> calls ask_for_confirmation()
    update_quantity: Searches for product by user input and changes the amount available
    get_total_inventory_value: Calculates the Sum of every product multiplied by quantity and price
    find_expired_products: Checks for expired products (food)
Other functions:
    product_factory: Factory method to create product objects based on category
    check_valid_date_input: Checks if the given date is in the correct format and if it is in the future.

"""

import sys
from stringcolor import cs
from datetime import datetime


"""
Package and Module Docstrings

Package docstrings should be placed at the top of the package’s __init__.py file. This docstring should list the modules and sub-packages that are exported by the package.

Module docstrings are similar to class docstrings. Instead of classes and class methods being documented, it’s now the module and any functions found within.
Module docstrings are placed at the top of the file even before any imports.
Module docstrings should include the following:


    A brief description of the module and its purpose
    A list of any classes, exception, functions, and any other objects exported by the module

The docstring for a module function should include the same items as a class method:

    A brief description of what the function is and what it’s used for
    Any arguments (both required and optional) that are passed including keyword arguments
    Label any arguments that are considered optional
    Any side effects that occur when executing the function
    Any exceptions that are raised
    Any restrictions on when the function can be called


Spreadsheet Column Printer

This script allows the user to print to the console all columns in the
spreadsheet. It is assumed that the first row of the spreadsheet is the
location of the columns.

This tool accepts comma separated value files (.csv) as well as excel
(.xls, .xlsx) files.

This script requires that `pandas` be installed within the Python
environment you are running this script in.

This file can also be imported as a module and contains the following
functions:

    * get_spreadsheet_cols - returns the column headers of the file
    * main - the main function of the script


"""


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


class LowPriceException(Exception):
    def __init__(self, message="Bad Price arguments"):
        self.message = message
        super().__init__(message)


class InventoryManager:
    def __init__(self, filename="database/products.json"):
        """
        Initialize the inventory manager.

        This method will load the product database from the
        predefined json file and store it in the attribute
        self.product_database. The attribute self.last_expiry_check
        will be set to a date far in the past.
        """
        self.filename = filename
        self.product_database = FileHandler.load_from_json(filename=filename)
        self.long_time_ago = "19.12.2024 12:00:00"
        self.last_expiry_check = datetime.strptime(
            self.long_time_ago, "%d.%m.%Y %H:%M:%S"
        )

    def search_product_by_user(self):
        """
        Ask for all information from the user to find specific products.
        When no input is given, it is skipped and a default value is assumed.
        """
        kwargs = {
            "make": None,
            "model": None,
            "low_price": 0,
            "high_price": None,
            "category": None,
            "colour": None,
        }
        while True:
            #  user input
            print(cs("Update filter arguments:", "blue"))
            print(
                cs(
                    f"Current filter for 'make': {kwargs['make']}. "
                    "Enter new value or leave empty to keep.",
                    "green",
                )
            )
            make_user_input = input("")
            if make_user_input:
                kwargs["make"] = make_user_input

            print(
                cs(
                    f"Current filter for 'model': {kwargs['model']}. "
                    "Enter new value or leave empty to keep.",
                    "green",
                )
            )
            model_user_input = input("")
            if model_user_input:
                kwargs["model"] = model_user_input

            print(
                cs(
                    f"Current filter for 'low_price': {kwargs['low_price']}. "
                    "Enter new value or leave empty to keep.",
                    "green",
                )
            )

            low_price_user_input = input("")
            if low_price_user_input:
                try:

                    low_price_user_input = float(low_price_user_input)

                    if low_price_user_input < 0:
                        low_price_user_input = 0
                    kwargs["low_price"] = low_price_user_input
                except ValueError:
                    print(
                        "Invalid input for low price. Input must be a digit --> Setting to Zero"
                    )
                    low_price_user_input = 0

            print(
                cs(
                    f"Current filter for 'high_price': {kwargs['high_price']}. "
                    "Enter new value or leave empty to keep.",
                    "green",
                )
            )

            high_price_user_input = input("")
            if high_price_user_input:
                try:
                    high_price_user_input = float(high_price_user_input)
                    if high_price_user_input < kwargs["low_price"]:
                        high_price_user_input = kwargs["low_price"] + 10
                        print(
                            "High price must be higher than low price"
                            f"--> Set to {high_price_user_input}"
                        )

                except ValueError:
                    print(
                        "Invalid input for high price. Input must be a digit"
                    )
                    high_price_user_input = float("inf")

            else:
                high_price_user_input = float("inf")
            kwargs["high_price"] = high_price_user_input

            print(
                cs(
                    f"Current filter for 'category': {kwargs['category']}. "
                    "Enter new value or leave empty to keep.",
                    "green",
                )
            )
            category_user_input = input("")
            if category_user_input:
                kwargs["category"] = category_user_input

            print(
                cs(
                    f"Current filter for 'colour': {kwargs['colour']}. "
                    "Enter new value or leave empty to keep.",
                    "green",
                )
            )
            colour_user_input = input("")
            if colour_user_input:
                kwargs["colour"] = colour_user_input

            # call search function
            search_result = self.search_product(**kwargs)
            print(cs(f"Keyword arguments are: {kwargs}", "lightGrey14"))
            if search_result:

                print(cs(f"Found {len(search_result)} products:", "Green"))
                for product in search_result:
                    print(product)
                end_result = search_result

            else:
                print(cs("No products found.", "Red2"))
                end_result = None

            return end_result

    def search_product(self, **kwargs):
        """
        Search for products in the inventory based on specified filters.

        Args:
            **kwargs: Optional filters including make, model, category, colour,
                    low_price, and high_price.

        Returns:
            A list of products that match the specified filters.
        """

        search_results = []

        make = kwargs.get("make")
        model = kwargs.get("model")
        category = kwargs.get("category")
        colour = kwargs.get("colour")
        low_price = kwargs.get("low_price")
        high_price = kwargs.get("high_price")

        search_results = self.product_database
        # If valid category is provided then drop all other categories
        # makes next step faster
        print(search_results)
        if category:
            search_results = list(
                filter(
                    lambda x: x["table_name"].lower() == category.lower(),
                    search_results,
                )
            )
        print(search_results)

        # Extract all single products from all records in all categories into products_list
        products_list = []
        for category_database in search_results:
            for product in category_database["records"]:
                products_list.append(product)

        # Search results is now a list of single products
        search_results = products_list
        print("search_results", search_results)
        # Filter by user input
        if colour:
            search_results = list(
                filter(
                    lambda x: colour.lower() in x["colour"].lower(),
                    search_results,
                )
            )
        if make:
            search_results = list(
                filter(
                    lambda x: make.lower() in x["make"].lower(), search_results
                )
            )
        if model:
            search_results = list(
                filter(
                    lambda x: model.lower() in x["model"].lower(),
                    search_results,
                )
            )
        if low_price:
            search_results = list(
                filter(lambda x: x["price"] >= low_price, search_results)
            )
        if high_price:
            search_results = list(
                filter(lambda x: x["price"] <= high_price, search_results)
            )
        print("---")
        print("search_results", search_results)

        return search_results

    def is_exist_product(self, make: str, model: str) -> bool:
        """
        Check if a product with the given make and model exists in the inventory.

        Args:
            make (str): The make of the product.
            model (str): The model of the product.

        Returns:
            bool: True if the product exists, False otherwise.
        """
        for item in self.product_database:

            if any(
                product["make"] == make and product["model"] == model
                for product in item["records"]
            ):

                return True

        return False

    def add_product(self):
        """Prompts the user to input details for a new product
        and adds it to the inventor if it doesn't already exist.
        Saves the updated inventory to a JSON file.
        """

        print("Please give details about new product:")
        make = input("make: ")
        model = input("Model: ")

        if not self.is_exist_product(make, model):
            category = input(
                "Category (electronics, food, apparel, household, toys, books): "
            )
            quantity = int(input("Quantity: "))
            price = float(input("Price: "))
            colour = input("Colour: ")

            kwargs = {
                "make": make,
                "model": model,
                "category": category,
                "quantity": quantity,
                "price": price,
                "colour": colour,
            }

            new_product = product_factory(**kwargs)
            if new_product:
                new_product_info = new_product.to_dict()

                for item in self.product_database:
                    if item["table_name"] == category:
                        item["records"].append(new_product_info)

                """ if category.lower() == "electronics":
                    new_product = Electronics(name=name, model=model, warranty_years=warranty_years, quantity=quantity, price=price, colour=colour)
                    new_product_info =  new_product.to_dict()
                    for item in self.product_database:
                        if item["table_name"] == "electronics":
                            item["records"].append(new_product_info) """

                FileHandler.save_to_json(self.product_database)

    def ask_for_confirmation(self, confirm_question):
        """
        Asks user to confirm an action and returns the user's choice.

        Parameters
        ----------
        confirm_question : str
            The question to ask the user for confirmation.

        Returns
        -------
        bool
            True if the user confirmed the action and False if the user
            chose to abort.
        """
        user_confirmation = False

        while not user_confirmation:
            user_choice = input(f"{confirm_question} Y/N")
            if user_choice == "n":
                print(cs("Removal aborted.....", "Grey"))
                user_confirmation = True
                user_confirmation_choice = False

            elif user_choice == "y":
                print(cs("Product record removed.....", "Green"))
                user_confirmation = True
                user_confirmation_choice = True

            else:
                print("Invalid choice, please enter Y/N.")
        return user_confirmation_choice

    def remove_product(self):
        """Remove existing product from inventory"""
        print("Please give details about product to delete:")
        make = input("make: ")
        model = input("Model: ")

        if self.is_exist_product(make, model):

            for item in self.product_database:

                for product in item["records"]:

                    if product["make"] == make and product["model"] == model:
                        print(product)
                        confirmed = self.ask_for_confirmation(
                            "Are you sure to telete the record?"
                        )
                        if confirmed:
                            item["records"].remove(product)
                        FileHandler.save_to_json(self.product_database)

    def update_quantity(self):
        """Update quantity of a product in inventory"""
        make = input("make: ")
        model = input("Model: ")

        if self.is_exist_product(make, model):

            for item in self.product_database:

                for product in item["records"]:

                    if product["make"] == make and product["model"] == model:
                        new_quantity = input(
                            f"Current quantity: {product['quantity']}\nNew quantity: "
                        )
                        new_quantity = int(new_quantity)
                        product["quantity"] = new_quantity
                        FileHandler.save_to_json(self.product_database)

    def get_total_inventory_value(self):
        """Calculate total value of the entire inventory"""
        total_inventory_value = 0

        for category_dabase in self.product_database:
            for record in category_dabase["records"]:

                if record.get("id"):
                    del record["id"]

                price_calc_object = product_factory(**record)
                total_inventory_value += price_calc_object.get_total_price()

        return total_inventory_value

    def find_expired_products(self):
        """Find the products and give out a list"""

        expired_products = []
        good_items = []
        current_time = datetime.now()
        for category_database in self.product_database:
            if category_database["table_name"] == "food":
                for item in category_database["records"]:
                    if current_time > datetime.strptime(
                        item["expiration_date"], "%d.%m.%Y %H:%M:%S"
                    ):
                        expired_products.append(item)
                    else:
                        good_items.append(item)

        if expired_products:
            for prod in expired_products:
                print(prod)
            choice_remove = input("Do you want to remove these items? Y/N")

            if choice_remove.lower() == "y":
                for category_database in self.product_database:
                    if category_database["table_name"] == "food":
                        category_database["records"] = good_items
                        FileHandler.save_to_json(self.product_database)

            elif choice_remove.lower() == "n":
                print("Ok someone will do it...someday!")
            else:
                print("No valid user choice. Return to main menu.")

        else:
            print("No products are expired.")
        self.last_expiry_check = datetime.now()
        return

    def remove_expired_products(self, expired_products):
        """Removes expired products from the inventory."""

        self.inventory_manager.last_expiry_check = datetime.now()


def product_factory(**kwargs):
    """Factory method to create
    product objects based on category"""

    category = kwargs["category"]

    del kwargs["category"]

    try:
        if category.lower() == "electronics":

            if not kwargs.get("warranty_years"):
                warranty_years = input("Warranty in years: ")

                kwargs["warranty_years"] = warranty_years

            return Electronics(**kwargs)

        elif category.lower() == "food":

            if not kwargs.get("Expiration date"):
                expiration_date = check_valid_date_input()
                if expiration_date:
                    kwargs["expiration_date"] = expiration_date
                else:
                    return
            return Food(**kwargs)

        elif category.lower() == "apparel":

            return Apparel(**kwargs)

        elif category.lower() == "household":

            return Household(**kwargs)

        elif category.lower() == "toys":

            return Toys(**kwargs)

        elif category.lower() == "book":

            if not kwargs.get("Author"):

                author = input("Author: ")

                kwargs["author"] = author

            return Book(**kwargs)

        else:

            raise ValueError("Invalid category")

    except ValueError as e:

        print(f"Error:{e}")

        return None


def check_valid_date_input():
    """
    Prompt the user to input a valid expiration date for a product.

    Checks if the given date is in the correct format and if it is in the future.
    If the user enters 'q', the function returns None.
    """
    while True:
        print("Dateformat should be like 01.01.2000 12:00:00")
        print("Please provide expiration date or  'q' to abort.\n")
        expiration_date = input("Expiration date: ")
        try:

            if expiration_date == "q":
                print("Add product aborted.")
                return None
            # Check if it its viable time format
            exp_date = datetime.strptime(expiration_date, "%d.%m.%Y %H:%M:%S")
            # Check if give date is in the future
            if exp_date > datetime.now():
                return expiration_date
            else:
                print(
                    "Expiration Date must be in the future. Please enter correct date information."
                )

        except ValueError as e:
            print(f"ValueError: {e}")


def main():
    """
    Main function to call for help
    Main function is there for you if you need it!

    """

    print()
    if len(sys.argv) == 2 and sys.argv[1] == "--help":
        print(__doc__)


if __name__ == "__main__":
    main()
