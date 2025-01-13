from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import json
import csv
from datetime import datetime


window = Tk()
window.title("Inventory Manager System")
window.geometry("1000x1000")
my_tree = ttk.Treeview(window, show="headings", height=20)
style = ttk.Style()
# id, make, name, price, quantity, category, colour, additional information
placeholder_array = ["", "", "", "", "", "", "", ""]
for i in range(0, 8):
    placeholder_array[i] = str()

    # id, make, name, price, quantity, category, colour, additional information
dummyData = [
    [123, "test", "test", "test", "test", "test", "test", "Tolkien (Author)"],
    [1223, "test", "test", "test", "test", "test", "test", "test"],
    [1243, "test", "test", "test", "test", "test", "test", "test", ""],
    [1213, "test", "test", "test", "test", "test", "test", "", "test"],
    [1253, "test", "test", "test", "test", "test", "test", "test", "test"],
    [12123, "test", "test", "test", "test", "test", "test", "test", ""],
    [123531, "test", "test", "test", "test", "test", "test", "test", "test"],
    [1233531, "test", "test", "test", "test", "test", "test", "test", ""],
    [1235531, "test", "test", "test", "test", "test", "test", "test", "test"],
    [123535731, "test", "test", "test", "test", "test", "test", "", ""],
    [12361531, "test", "test", "test", "test", "test", "test", "test", "test"],
    [1273531, "test", "test", "test", "test", "test", "test", "test", "test"],
    [1232475531, "test", "test", "test", "test", "test", "test", "test", ""],
    [12351331, "test", "test", "test", "test", "test", "test", "test", "test"],
    [123547231, "test", "test", "test", "test", "test", "test", "test", "test"],
    [4, "test", "test", "test", "test", "test", "test", "test", "test"],
    [12354231, "test", "test", "test", "test", "test", "test", "test", "test"],
    [1232531, "test", "test", "test", "test", "test", "test", "test", ""],
    [1238531, "test", "test", "test", "test", "test", "test", "test", "test"],
    [12353841, "test", "test", "test", "test", "test", "test", "test", ""],
    [2352431, "test", "test", "test", "test", "test", "test", "test"],
    [123473531, "test", "test", "test", "test", "test", "test", "test", ""],
]


def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)

    for array in dummyData:
        my_tree.insert(
            parent="", index="end", iid=array, text="", values=(array), tag="orow"
        )
    my_tree.tag_configure("orow", background="#EEEEEE")
    my_tree.pack()


# def generate_ID():
#     category = category_Combo.get()
#     if category in category_Array:
#         if category_Array.index(category) == 0:
#             ID = random.randint(10000, 99999)
#             return f"Ap+{ID}"
#         elif category_Array.index(category) == 1:
#             ID = random.randint(10000, 99999)
#             return f"Ap+{ID}"
#         elif category_Array.index(category) == 2:
#             ID = random.randint(10000, 99999)
#             return f"Ap+{ID}"
#         elif category_Array.index(category) == 3:
#             ID = random.randint(10000, 99999)
#             return f"Ap+{ID}"
#         elif category_Array.index(category) == 4:
#             ID = random.randint(10000, 99999)
#             return f"Ap+{ID}"
#         else:
#             return ""


frame = Frame(window, bg="#02577A")
frame.pack()

button_colour = "#196E78"
manage_Frame = LabelFrame(frame, text="Manage", borderwidth=5)
manage_Frame.grid(row=0, column=0, sticky="w", padx=[10, 200], pady=[10, 20], ipadx=[6])

saveButton = Button(
    manage_Frame,
    fg="white",
    text="Save",
    width=10,
    borderwidth=3,
    bg=button_colour,
    command=lambda: print("save"),
)
updateButton = Button(
    manage_Frame,
    fg="white",
    text="Update",
    width=10,
    borderwidth=3,
    bg=button_colour,
    command=lambda: print("update"),
)
deleteButton = Button(
    manage_Frame,
    fg="white",
    text="Delete",
    width=10,
    borderwidth=3,
    bg=button_colour,
    command=lambda: print("delete"),
)
selectButton = Button(
    manage_Frame,
    fg="white",
    text="Select",
    width=10,
    borderwidth=3,
    bg=button_colour,
    command=lambda: print("select"),
)
findButton = Button(
    manage_Frame,
    fg="white",
    text="Find",
    width=10,
    borderwidth=3,
    bg=button_colour,
    command=lambda: print("find"),
)
clearButton = Button(
    manage_Frame,
    fg="white",
    text="Clear",
    width=10,
    borderwidth=3,
    bg=button_colour,
    command=lambda: print("clear"),
)

saveButton.grid(row=0, column=0, padx=10, pady=10)
updateButton.grid(row=0, column=1, padx=10, pady=10)
deleteButton.grid(row=0, column=2, padx=10, pady=10)
selectButton.grid(row=0, column=3, padx=10, pady=10)
findButton.grid(row=0, column=4, padx=10, pady=10)
clearButton.grid(row=0, column=5, padx=10, pady=10)

entries_Frame = LabelFrame(frame, text="Entries", borderwidth=5)
entries_Frame.grid(
    row=1, column=0, sticky="w", padx=[10, 200], pady=[10, 20], ipadx=[6]
)

# id, make, name, price, quantity, category, colour, additional information
itemId_Label = Label(entries_Frame, text="Item ID")
make_Label = Label(entries_Frame, text="Make")
name_Label = Label(entries_Frame, text="Name")
price_Label = Label(entries_Frame, text="Price")
quantity_Label = Label(entries_Frame, text="Quantity")
category_Label = Label(entries_Frame, text="Category")
colour_Label = Label(entries_Frame, text="Colour")
additional_Label = Label(entries_Frame, text="Additional Information")
clarification_Label = Label(entries_Frame, text="(Book, Elec., Food)")

itemId_Label.grid(row=0, column=0, padx=10, pady=10)
make_Label.grid(row=1, column=0, padx=10, pady=10)
name_Label.grid(row=2, column=0, padx=10, pady=10)
price_Label.grid(row=3, column=0, padx=10, pady=10)
quantity_Label.grid(row=4, column=0, padx=10, pady=10)
category_Label.grid(row=5, column=0, padx=10, pady=10)
colour_Label.grid(row=6, column=0, padx=10, pady=10)
additional_Label.grid(row=7, column=0, padx=10, pady=10)
clarification_Label.grid(row=7, column=3, padx=10, pady=10)

# https://youtu.be/XwDwB4JsTZM?feature=shared&t=556
# region Entries
category_Array = ["Apparel", "Book", "Electronics", "Food", "Household", "Toys"]

itemId_Entry = Entry(entries_Frame, width=50, textvariable=placeholder_array[0])
make_Entry = Entry(entries_Frame, width=50, textvariable=placeholder_array[1])
name_Entry = Entry(entries_Frame, width=50, textvariable=placeholder_array[2])
price_Entry = Entry(entries_Frame, width=50, textvariable=placeholder_array[3])
quantity_Entry = Entry(entries_Frame, width=50, textvariable=placeholder_array[4])
category_Combo = ttk.Combobox(
    entries_Frame,
    width=49,
    textvariable=placeholder_array[5],
    values=category_Array,
)
category_Combo.set("Apparel")
colour_Entry = Entry(entries_Frame, width=50, textvariable=placeholder_array[6])
additional_Label = Entry(
    entries_Frame,
    width=50,
    textvariable=f"{placeholder_array[7]}",
)

itemId_Entry.grid(row=0, column=2, padx=5, pady=5)
make_Entry.grid(row=1, column=2, padx=5, pady=5)
name_Entry.grid(row=2, column=2, padx=5, pady=5)
price_Entry.grid(row=3, column=2, padx=5, pady=5)
quantity_Entry.grid(row=4, column=2, padx=5, pady=5)
category_Combo.grid(row=5, column=2, padx=5, pady=5)
colour_Entry.grid(row=6, column=2, padx=5, pady=5)
additional_Label.grid(row=7, column=2, padx=5, pady=5)

generateIdButton = Button(
    entries_Frame, text="Generate ID", borderwidth=3, bg=button_colour, fg="white"
)
generateIdButton.grid(row=0, column=3, padx=5, pady=5)
# endregion

style.configure(window)

my_tree["columns"] = (
    "Item Id",
    "Make",
    "Name",
    "Price",
    "Quantity",
    "Category",
    "Colour",
    "Additional Information",
)
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Item Id", anchor=W, width=70)
my_tree.column("Make", anchor=W, width=100)
my_tree.column("Name", anchor=W, width=130)
my_tree.column("Price", anchor=W, width=100)
my_tree.column("Quantity", anchor=W, width=150)
my_tree.column("Category", anchor=W, width=150)
my_tree.column("Colour", anchor=W, width=100)
my_tree.column("Additional Information", anchor=W, width=200)

my_tree.heading("Item Id", text="Item Id", anchor=W)
my_tree.heading("Make", text="Make", anchor=W)
my_tree.heading("Name", text="Name", anchor=W)
my_tree.heading("Price", text="Price", anchor=W)
my_tree.heading("Quantity", text="Quantity", anchor=W)
my_tree.heading("Category", text="Category", anchor=W)
my_tree.heading("Colour", text="Colour", anchor=W)
my_tree.heading("Additional Information", text="Additional Information", anchor=W)

my_tree.tag_configure("orow", background="#EEEEEE")
my_tree.pack()

refreshTable()
# window.withdraw() <-- to hide a window
# window.deiconify() <-- to show a window
window.resizable(False, False)
window.mainloop()
