import tkinter as tk
from tkinter import messagebox
import pickle

# Contact Book Class
class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        self.contacts[name] = {"Phone": phone, "Email": email, "Address": address}

    def get_contacts(self):
        return self.contacts

    def search_contact(self, key):
        return self.contacts.get(key, None)

    def update_contact(self, name, phone, email, address):
        if name in self.contacts:
            self.contacts[name] = {"Phone": phone, "Email": email, "Address": address}
            return True
        return False

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            return True
        return False

    def save_contacts(self, filename="contacts.pkl"):
        with open(filename, "wb") as file:
            pickle.dump(self.contacts, file)

    def load_contacts(self, filename="contacts.pkl"):
        try:
            with open(filename, "rb") as file:
                self.contacts = pickle.load(file)
        except FileNotFoundError:
            self.contacts = {}

# Initialize Contact Book
book = ContactBook()
book.load_contacts()

# Functions for GUI
def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if name and phone:
        book.add_contact(name, phone, email, address)
        book.save_contacts()
        update_contact_list()
        messagebox.showinfo("Success", f"Contact '{name}' added successfully!")
        clear_entries()
    else:
        messagebox.showerror("Error", "Name and Phone are required!")

def update_contact_list():
    contact_list.delete(0, tk.END)
    for name, details in book.get_contacts().items():
        contact_list.insert(tk.END, f"{name} - {details['Phone']}")

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def search_contact():
    search_key = name_entry.get().strip()
    result = book.search_contact(search_key)
    if result:
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)
        phone_entry.insert(0, result["Phone"])
        email_entry.insert(0, result["Email"])
        address_entry.insert(0, result["Address"])
    else:
        messagebox.showinfo("Not Found", f"No contact found for '{search_key}'")

def update_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if name and book.update_contact(name, phone, email, address):
        book.save_contacts()
        update_contact_list()
        messagebox.showinfo("Success", f"Contact '{name}' updated successfully!")
        clear_entries()
    else:
        messagebox.showerror("Error", f"Contact '{name}' not found!")

def delete_contact():
    selected = contact_list.curselection()
    if selected:
        contact = contact_list.get(selected[0]).split(" - ")[0]
        if book.delete_contact(contact):
            book.save_contacts()
            update_contact_list()
            messagebox.showinfo("Success", f"Contact '{contact}' deleted successfully!")
    else:
        messagebox.showerror("Error", "Select a contact to delete!")

# GUI Design
app = tk.Tk()
app.title("Contact Book")
app.geometry("600x500")
app.config(bg="#ecf0f1")

# Entry Fields
frame = tk.Frame(app, bg="#ecf0f1")
frame.pack(pady=10)

tk.Label(frame, text="Name:", font=("Arial", 12), bg="#ecf0f1").grid(row=0, column=0, padx=5, pady=5, sticky="e")
name_entry = tk.Entry(frame, width=30, font=("Arial", 12))
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Phone:", font=("Arial", 12), bg="#ecf0f1").grid(row=1, column=0, padx=5, pady=5, sticky="e")
phone_entry = tk.Entry(frame, width=30, font=("Arial", 12))
phone_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="Email:", font=("Arial", 12), bg="#ecf0f1").grid(row=2, column=0, padx=5, pady=5, sticky="e")
email_entry = tk.Entry(frame, width=30, font=("Arial", 12))
email_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame, text="Address:", font=("Arial", 12), bg="#ecf0f1").grid(row=3, column=0, padx=5, pady=5, sticky="e")
address_entry = tk.Entry(frame, width=30, font=("Arial", 12))
address_entry.grid(row=3, column=1, padx=5, pady=5)

# Buttons
button_frame = tk.Frame(app, bg="#ecf0f1")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add", font=("Arial", 12), bg="#2ecc71", fg="white", command=add_contact).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="Search", font=("Arial", 12), bg="#3498db", fg="white", command=search_contact).grid(row=0, column=1, padx=10)
tk.Button(button_frame, text="Update", font=("Arial", 12), bg="#f1c40f", fg="white", command=update_contact).grid(row=0, column=2, padx=10)
tk.Button(button_frame, text="Delete", font=("Arial", 12), bg="#e74c3c", fg="white", command=delete_contact).grid(row=0, column=3, padx=10)

# Contact List
contact_list = tk.Listbox(app, font=("Arial", 12), height=12, width=50)
contact_list.pack(pady=10)

# Initialize the contact list display
update_contact_list()

# Run the app
app.mainloop()
