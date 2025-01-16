"""Main Inventory Manager Function"""

from inventory_manager.inventory_manager import InventoryManager
from stringcolor import cs
import user_database.user_database as user_db
from datetime import datetime, timedelta
from getpass import getpass


class Main:
    def __init__(self) -> None:
        """
        Initializes the main menu of the Inventory Manager System.

        The main menu is defined by self.options, which is a dictionary of
        options that the user can choose from. The keys of the dictionary
        are the option numbers, and the values are the functions that are
        called when the option is chosen.

        The function also initializes the InventoryManager object, which
        is responsible for managing the products in the inventory.
        """
        self.options = {
            "1": self.register_account,
            "2": self.log_in,
            "3": self.exit_program,
        }
        self.inventory_manager = InventoryManager()

    def display(self):
        """
        Displays the main menu of the Inventory Manager System
        and waits for user input.

        The main menu is displayed in a loop, until the user
        chooses to exit the program.

        The options are:

        1. Register a new account
        2. Log in to your existing account
        3. Exit

        When the user chooses an option,
        the corresponding function is called, and the
        loop continues.
        """
        while True:
            print()
            print(cs("****************************", "DarkMagenta2"))
            print("Welcome to the Inventory Manager System")
            print("1. Register a new account")
            print("2. Log in to your existing account")
            print("3. Exit")
            print(cs("****************************", "DarkMagenta2"))
            self.get_input()

    def get_input(self):
        prompt = input("Enter choice: ")
        if prompt in self.options:
            self.options[prompt]()
        else:
            print("Invalid choice")

    def register_account(self):
        username = input("username: ")
        password = getpass("password: ")
        role = "user"
        user_db.register_user(username, password, role)

    def log_in(self):
        username = input("username: ")
        password = getpass("password: ")
        user_role = user_db.login_user(username, password)
        if user_role:
            logged = LogIn(self, self.inventory_manager, user_role)
            logged.display()

    def exit_program(self):
        print("Exiting the program. Goodbye!")
        exit()


class LogIn:
    def __init__(
        self, main_menu, inventory_manager, user_role, *args, **kwargs
    ) -> None:
        self.inventory_manager = inventory_manager
        self.user_role = user_role
        if self.user_role == "admin":
            self.options = {
                "1": self.search_product,
                "2": self.add_product,
                "3": self.remove_product,
                "4": self.update_quantity,
                "5": self.inventory_value,
                "6": self.back_to_main_menu,
                "7": self.exit_program,
                "8": self.create_user,
                "9": self.show_users,
                "10": self.remove_user,
                "11": self.find_expired_product,
            }
        elif self.user_role == "user":
            self.options = {
                "1": self.search_product,
                "2": self.add_product,
                "3": self.remove_product,
                "4": self.update_quantity,
                "5": self.inventory_value,
                "6": self.back_to_main_menu,
                "7": self.exit_program,
            }
        else:
            print("Invalid role choice.")
        self.main_menu = main_menu  # Store the main menu

    def display(self):

        while True:

            last_check = datetime.strftime(
                self.inventory_manager.last_expiry_check, "%d.%m.%Y %H:%M:%S"
            )

            current_time = datetime.now()
            time_since_last_check = (
                current_time - self.inventory_manager.last_expiry_check
            )
            warning_expiry = timedelta(days=1)

            if time_since_last_check > warning_expiry:
                print(cs("Reminder: Check expired products!", "Orange"))
                user_choice = input("Do you want to check now? y/n: ")
                if user_choice == "y":
                    self.inventory_manager.find_expired_products()

            print()
            if self.user_role == "admin":
                print(cs("****************************", "SteelBlue2"))
                print("Please choose an option:")
                print("1. Search products")
                print("2. Add product")
                print("3. Remove product")
                print("4. Update quantity of a product")
                print("5. Get total inventory value")
                print("6. Back to main menu")
                print("7. Exit program")
                print("8. Create user")
                print("9. Show users")
                print("10. Remove user")
                print("11. find_expired_products")
                print(cs("****************************", "SteelBlue2"))
                self.get_input()

            elif self.user_role == "user":
                print(cs("****************************", "SteelBlue2"))
                print("Please choose an option:")
                print("1. Search products")
                print("2. Add product")
                print("3. Remove product")
                print("4. Update quantity of a product")
                print("5. Get total inventory value")
                print("6. Back to main menu")
                print("7. Exit program")
                print(cs("****************************", "SteelBlue2"))
                self.get_input()
            else:
                self.main_menu.display()

    def get_input(self):
        prompt = input("Enter choice: ")
        if prompt in self.options:
            self.options[prompt]()
        else:
            print(cs("Invalid choice", "Red"))

    def search_product(self):
        self.inventory_manager.search_product_by_user()

    def add_product(self):
        self.inventory_manager.add_product()

    def remove_product(self):
        self.inventory_manager.remove_product()

    def update_quantity(self):
        self.inventory_manager.update_quantity()

    def inventory_value(self):
        total_inventory_value = (
            self.inventory_manager.get_total_inventory_value()
        )
        print(
            cs(f"Total inventory value: {total_inventory_value}", "DarkOrange")
        )

    def back_to_main_menu(self):
        self.main_menu.display()

    def exit_program(self):
        print("Exiting the program. Goodbye!")
        exit()

    def create_user(self):
        username = input("username: ")
        password = input("password: ")
        role = input("admin/user")
        if role in ["admin", "user"]:
            user_db.register_user(username, password, role)
        else:
            print("Invalid role choice.")

    def show_users(self):
        user_db.view_all_users()

    def remove_user(self):
        user_db.remove_user()

    def find_expired_product(self):
        self.inventory_manager.find_expired_products()


def main():
    main = Main()
    main.display()


if __name__ == "__main__":
    main()
