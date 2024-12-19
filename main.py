"""Main Inventory Manager Function"""

from inventory_manager.inventory_manager import InventoryManager
from stringcolor import cs
import user_database.user_database as user_db
from datetime import datetime, timedelta

class Main:
    def __init__(self) -> None:
        self.options = {
            "1": self.register_account,
            "2": self.log_in,
            "3": self.exit_program,
        }
        self.inventory_manager = InventoryManager()

    def display(self):
        while True:
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
        pass

    def log_in(self):
        # [x] TODO Check if login is correct ...
        username = input("username: ")
        password = input("password: ")
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

            last_check = datetime.strftime(self.inventory_manager.last_expiry_check, "%d.%m.%Y %H:%M:%S")
            print(last_check)

            current_time = datetime.now()
            time_since_last_check = current_time - self.inventory_manager.last_expiry_check
            print(type(time_since_last_check))

            warning_expiry = timedelta(days=1)
            if time_since_last_check > warning_expiry:
                print("Check expired products!")
            # Todo check expirateion dates ....
            # method remove expired products
            # self.inventory_manager.last_expiry_check = datetime.now()

            # [ ] TODO clean up duplicate code
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
            print("Invalid choice")

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


# def main():

# inventory_manager = InventoryManager()

# # im.add_product()
# # print(im.search_product_by_user())

# while True:
#     print("\nInventory Manager v.1.0\n")
#     print("1. Register new user")
#     print("2. Login")
#     print("3. Exit")
#     choice = input("Enter 1, 2, or 3\n")

#     if choice == "1":
#         pass

#     elif choice == "2":
#         user = "bob"
#         if user:
#             print("Login successful")
#             while True:
#                 print("\nPlease choose from the following choices:\n")
#                 print("1. Search for a product in inventory")
#                 print("2. Add a new product to inventory")
#                 print("3. Remove a product from inventory")
#                 print(
#                     "4. Update quantity of existing product in inventory"
#                 )
#                 print("5. Calculate total value of inventory")
#                 print("X. Logout")
#                 user_choice = input(
#                     "Enter 1, 2, 3, 4, 5, or 'X' to logout: "
#                 )

#                 if user_choice == "1":
#                     inventory_manager.search_product_by_user()

#                 elif user_choice == "2":
#                     inventory_manager.add_product()

#                 elif user_choice == "3":
#                     inventory_manager.remove_product()

#                 elif user_choice == "4":
#                     inventory_manager.update_quantity()

#                 elif user_choice == "5":
#                     inventory_manager.get_total_inventory_value

#                 elif user_choice.lower == "X":
#                     print("Logout Successful")
#                     return

#                 else:
#                     print(
#                         "Login failed. Please check your username or password."
#                     )

#     elif choice == "3":
#         confirm = input("Are you sure you want to exit? (y/n): ")
#         if confirm.lower() == "y":
#             print("Goodbye.")
#             break

#         else:
#             print("Invalid entry, try again.")


def main():
    main = Main()
    main.display()


if __name__ == "__main__":
    main()
