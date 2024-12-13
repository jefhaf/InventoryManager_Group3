from inventory_manager.inventory_manager import InventoryManager



"""Main Inventory Manager Function"""


def main():
    while True:
        print("\nInventory Manager v.1.0\n")
        print("1. Register new user")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter 1, 2, or 3\n")

        if choice == '1':
            pass

        elif choice == '2':
            user = 
            if user:
                print("Login successful")
                while True:
                    print("\nPlease choose from the following choices:\n")
                    print("1. Search for a product in inventory")
                    print("2. Add a new product to inventory")
                    print("3. Remove a product from inventory")
                    print("4. Update quantity of existing product in inventory")
                    print("5. Calculate total value of inventory")
                    print("X. Logout")
                    user_choice = input("Enter 1, 2, 3, 4, 5, or 'X' to logout: ")

                    if user_choice == '1':
                        InventoryManager.search_product()

                    elif user_choice == '2':
                        InventoryManager.add_product()

                    elif user_choice == '3':
                        InventoryManager.remove_product()

                    elif user_choice == '4':
                        InventoryManager.update_quantity()

                    elif user_choice == '5':
                        InventoryManager.get_total_inventory_value

                    elif user_choice.lower == 'X':
                        print("Logout Successful")
                        break

                    else:
                        print("Login failed. Please check your username or password.")

        elif choice == '3':
            confirm = input("Are you sure you want to exit? (y/n): ")
            if confirm.lower() == 'y':
                print("Goodbye.")
                break

            else:
                print("Invalid entry, try again.")


if __name__ == "__main__":
    main()
