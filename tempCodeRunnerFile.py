import tkinter as tk
from tkinter import messagebox

class ContactManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Management System")
        self.root.configure(bg='lightgray')  # Set background color to blue

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
        tk.Button(self.root, text="Add Contact", command=self.add_contact, font=('Arial', 14), bg='#2ecc71', fg='white').grid(row=3, column=1, pady=15, padx=15, sticky=tk.E)
        tk.Button(self.root, text="View Contacts", command=self.view_contacts, font=('Arial', 14), bg='#2ecc71', fg='white').grid(row=4, column=1, pady=15, padx=15, sticky=tk.E)
        tk.Button(self.root, text="Search Contact", command=self.search_contact, font=('Arial', 14), bg='#2ecc71', fg='white').grid(row=5, column=1, pady=15, padx=15, sticky=tk.E)
        tk.Button(self.root, text="Update Contact", command=self.update_contact, font=('Arial', 14), bg='#2ecc71', fg='white').grid(row=6, column=1, pady=15, padx=15, sticky=tk.E)
        tk.Button(self.root, text="Delete Contact", command=self.delete_contact, font=('Arial', 14), bg='#e74c3c', fg='white').grid(row=7, column=1, pady=15, padx=15, sticky=tk.E)


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagementSystem(root)
    root.mainloop()