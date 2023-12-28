import tkinter as tk
from tkinter import messagebox

class ContactManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Management System")
        self.root.configure(bg='lightgray')  

        self.contacts = {}

        self.create_widgets()

    def create_widgets(self):
        # Labels and Entry Widgets
        tk.Label(self.root, text="Name:", font=('Arial', 14),fg='blue').grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)
        self.name_entry = tk.Entry(self.root, font=('Arial', 14))
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Surname:", font=('Arial', 14), fg='blue').grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)
        self.surname_entry = tk.Entry(self.root, font=('Arial', 14))
        self.surname_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Number:", font=('Arial', 14), fg='blue').grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)
        self.number_entry = tk.Entry(self.root, font=('Arial', 14))
        self.number_entry.grid(row=2, column=1, padx=10, pady=10)

        # Buttons
        tk.Button(self.root, text="Add Contact", command=self.add_contact, font=('Arial', 14), fg='green').grid(row=3, column=1, pady=15, padx=15, sticky=tk.E)
        tk.Button(self.root, text="View Contacts", command=self.view_contacts, font=('Arial', 14), fg='green').grid(row=4, column=1, pady=15, padx=15, sticky=tk.E)
        tk.Button(self.root, text="Search Contact", command=self.search_contact, font=('Arial', 14), fg='green').grid(row=5, column=1, pady=15, padx=15, sticky=tk.E)
        tk.Button(self.root, text="Update Contact", command=self.update_contact, font=('Arial', 14),  fg='green').grid(row=6, column=1, pady=15, padx=15, sticky=tk.E)
        tk.Button(self.root, text="Delete Contact", command=self.delete_contact, font=('Arial', 14), fg='red').grid(row=7, column=1, pady=15, padx=15, sticky=tk.E)

    def add_contact(self):
        name = self.name_entry.get()
        surname = self.surname_entry.get()
        number = self.number_entry.get()

        if name and number:
            full_name = f"{name} {surname}"
            self.contacts[full_name] = number
            messagebox.showinfo("Success", f"Contact '{full_name}' added successfully!")
        else:
            messagebox.showerror("Error", "Please enter both name and number.")

        # Clear the entry fields
        self.name_entry.delete(0, tk.END)
        self.surname_entry.delete(0, tk.END)
        self.number_entry.delete(0, tk.END)

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("No Contacts", "No contacts found.")
        else:
            contact_list = "\n".join([f"{name}: {number}" for name, number in self.contacts.items()])
            messagebox.showinfo("Contacts", contact_list)

    def search_contact(self):
        name = self.name_entry.get()
        surname = self.surname_entry.get()

        full_name = f"{name} {surname}"

        if full_name in self.contacts:
            messagebox.showinfo("Contact Found", f"{full_name}: {self.contacts[full_name]}")
        else:
            messagebox.showinfo("Contact Not Found", f"Contact '{full_name}' not found.")

        # Clear the entry fields
        self.name_entry.delete(0, tk.END)
        self.surname_entry.delete(0, tk.END)

    def update_contact(self):
        name = self.name_entry.get()
        surname = self.surname_entry.get()
        number = self.number_entry.get()

        full_name = f"{name} {surname}"

        if full_name in self.contacts:
            self.contacts[full_name] = number
            messagebox.showinfo("Success", f"Contact '{full_name}' updated successfully!")
        else:
            messagebox.showinfo("Contact Not Found", f"Contact '{full_name}' not found.")

        # Clear the entry fields
        self.name_entry.delete(0, tk.END)
        self.surname_entry.delete(0, tk.END)
        self.number_entry.delete(0, tk.END)

    def delete_contact(self):
        name = self.name_entry.get()
        surname = self.surname_entry.get()

        full_name = f"{name} {surname}"

        if full_name in self.contacts:
            del self.contacts[full_name]
            messagebox.showinfo("Success", f"Contact '{full_name}' deleted successfully!")
        else:
            messagebox.showinfo("Contact Not Found", f"Contact '{full_name}' not found.")

        # Clear the entry fields
        self.name_entry.delete(0, tk.END)
        self.surname_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagementSystem(root)
    root.mainloop()
