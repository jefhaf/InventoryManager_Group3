import sys
from stringcolor import cs

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

    def search_product_by_user(self):
        # [x] TODO give initial default filter parameters
        # [x] TODO make clear its a filter (instad of search)
        # [x] TODO provide current filter argument and ask user if he wants to change the filter argument

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
                        "Invalid input for low price. Input must be a digit."
                    )

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
                    if high_price_user_input:
                        high_price_user_input = float(high_price_user_input)
                    else:
                        high_price_user_input = None
                    kwargs["high_price"] = high_price_user_input
                except ValueError:
                    print(
                        "Invalid input for high price. Input must be a digit"
                    )

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

            search_result = self.search_product(**kwargs)
            if search_result:
                print(cs(f"Keyword arguments are: {kwargs}", "lightGrey14"))
                print(cs(f"Found {len(search_result)} products:", "Green"))
                for product in search_result:
                    print(product)

            else:
                print(cs("No products found.", "Red2"))

            valid_user_choice = False

            while not valid_user_choice:

                print("Do you want to continue with the search?")

                user_choice = input("Y/N: ").lower()

                if user_choice == "n":

                    return "Exiting....."

                elif user_choice == "y":

                    valid_user_choice = True

                else:

                    print("Invalid choice, please enter Y/N.")

        # call search function

    def search_product(self, **kwargs):
        """Search for product in inventory by matching any field."""
        search_results = []

        make = kwargs.get("make")
        model = kwargs.get("model")
        category = kwargs.get("category")
        colour = kwargs.get("colour")
        low_price = kwargs.get("low_price")
        high_price = kwargs.get("high_price")

        for category_database in self.product_database:

            only_category = category and not any(
                [make, model, colour, low_price, high_price]
            )

            if (
                only_category
                and category.lower() in category_database["table_name"].lower()
            ):
                search_results.extend(category_database["records"])

            for product in category_database["records"]:

                if (
                    (make and make.lower() in product["make"].lower())
                    or (model and model.lower() in product["model"].lower())
                    or (colour and colour.lower() in product["colour"].lower())
                    or (
                        (
                            low_price is not None
                            and product["price"] >= low_price
                        )
                        and (
                            high_price is not None
                            and product["price"] <= high_price
                        )
                    )
                ):
                    search_results.append(product)

        return search_results

    def is_exist_product(self, make: str, model: str) -> bool:

        for item in self.product_database:

            if any(
                product["make"] == make and product["model"] == model
                for product in item["records"]
            ):

                return True

        return False

    def add_product(self):
        """add new product to inventory"""
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

    def ask_for_confirmation(self, confirm_question):
        user_confirmation = False

        while not user_confirmation:
            user_choice = input(
                f"Are you sure you want to {confirm_question}? Y/N"
            )
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
        # TODO use search function  and give option to choose result for removal

        if self.is_exist_product(make, model):

            for item in self.product_database:

                for product in item["records"]:

                    if product["make"] == make and product["model"] == model:
                        # TODO Ask for confirmation
                        print(product)
                        confirmed = self.ask_for_confirmation(
                            "delete the product record"
                        )
                        if confirmed:
                            item["records"].remove(product)
                        FileHandler.save_to_json(self.product_database)

    def update_quantity(self):
        """Update quantity of a product in inventory"""
        make = input("make: ")
        model = input("Model: ")
        # TODO use search function  and give option to choose result for removal

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
                print(record)
                print()
                if record.get("id"):
                    del record["id"]

                price_calc_object = product_factory(**record)
                total_inventory_value += price_calc_object.get_total_price()

        return total_inventory_value

    def validate_database(self):
        """Check for any missing data or wrong datatypes in all entries of database"""
        pass


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
                expiration_date = input("Expiration date")
                # [ ] TODO Check valid date
                kwargs["expiration_date"] = expiration_date

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


def main():
    # Create insctance of InventoryManager
    im = inventory_manager()

    print(im.product_database)

    # im.add_product()
    # print(im.search_product_by_user())
    print()


# im_test()

if __name__ == "__main__":
    main()
