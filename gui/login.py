import tkinter
from tkinter import messagebox


# Validate Login
def validate_login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "admin":
        messagebox.showinfo(title="Login successful",
                            message="Welcome, Admin!")
    else:
        messagebox.showerror(title="Login failed",
                            message="Invalid username or password")


# Main Window
window = tkinter.Tk()
window.title("Inventory Manager System")
window.geometry('300x150')
window.configure(bg="#333333")

login_label = tkinter.Label(window, text="Login", bg="#333333", fg="#FFFFFF")

username_label = tkinter.Label(
    window, text="Username", bg="#333333", fg="#FFFFFF")

# Username input
username_entry = tkinter.Entry(window)

password_label = tkinter.Label(
    window, text="Password", bg="#333333", fg="#FFFFFF")

# Password input(hidden)
password_entry = tkinter.Entry(window, show="*")

login_button = tkinter.Button(
    window, text="Login", borderwidth=3, bg="#196E78", fg="#FFFFFF", command=validate_login)

login_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
username_label.grid(row=1, column=0, padx=5, pady=5)
username_entry.grid(row=1, column=1, padx=5, pady=5)
password_label.grid(row=2, column=0, padx=5, pady=5)
password_entry.grid(row=2, column=1, padx=5, pady=5)
login_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

window.mainloop()
