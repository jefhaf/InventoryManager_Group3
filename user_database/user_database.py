import json
from passlib.context import CryptContext

# Create a CryptContext instance to handle password hashing and verification
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# File where user credentials will be stored
USERS_FILE = "user_database/users.json"


# Load existing users from the JSON file
def load_users():
    try:
        with open(USERS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}  # Return an empty dictionary if the file doesn't exist yet


# Save users to the JSON file
def save_users(users):
    with open(USERS_FILE, "w") as file:
        json.dump(users, file, indent=4)


# Hash a password
def hash_password(password: str) -> str:
    return pwd_context.hash(password)


# Verify the password
def verify_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)


# Register a new user
# Register a new user with a role
def register_user(username: str, password: str, role: str = "user"):
    users = load_users()  # Load existing users
    if username in users:
        print("Username already exists.")
        return False

    # Hash the user's password
    hashed_password = hash_password(password)

    # Add the new user with role to the users dictionary
    users[username] = {"password": hashed_password, "role": role}

    # Save the updated users to the file
    save_users(users)
    print(f"User '{username}' registered successfully with role '{role}'!")
    return True


# Login a user
# Login a user and get their role
def login_user(username: str, password: str):
    users = load_users()  # Load existing users
    if username not in users:
        print("Username not found.")
        return None  # Return None if user is not found

    # Verify the entered password against the stored hashed password
    hashed_password = users[username]["password"]
    if verify_password(password, hashed_password):
        print(f"Welcome, {username}!")

        # Access the role of the user and store it in a variable
        user_role = users[username]["role"]

        print(f"Your role: {user_role}")
        return user_role  # Return the role of the user
    else:
        print("Incorrect password. Please contact management.")
        return None  # Return None if password is incorrect


# Display all users (only accessible by admins)
def view_all_users():
    users = load_users()  # Load all users
    if not users:
        print("No users found.")
        return

    print("\nList of all users:")
    for username, user_data in users.items():
        print(f"Username: {username}, Role: {user_data['role']}")


# Remove a user (only accessible by admins)
def remove_user():
    users = load_users()  # Load all users
    username = input("Enter the username of the user to remove: ")

    if username not in users:
        print(f"User '{username}' not found.")
        return

    # Confirm the deletion
    confirmation = input(
        f"Are you sure you want to remove the user '{username}'? (y/n): "
    )
    if confirmation.lower() == "y":
        del users[username]  # Remove the user from the dictionary
        save_users(users)  # Save the updated users back to the file
        print(f"User '{username}' has been removed.")
    else:
        print(f"User '{username}' was not removed.")


# Example usage
if __name__ == "__main__":
    # Register new users
    register_user("admin", "admin")

    # Attempt to login
    login_user("admin", "admin")  # Should be successful
