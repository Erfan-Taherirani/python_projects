from tabulate import tabulate
from rich import print as rprint


class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email=None, address=None):
        if name not in self.contacts:
            self.contacts[name] = {
                "phone": phone,
                "email": email,
                "address": address
            }
            rprint("[red bold]Contact Created.")
            
        else:
            rprint("[red bold]Contact Already Exists!")

    def list_contacts(self):
        rprint("\n\n[blue bold]List of Contacts:")
        table = [["Name", "Phone Number", "Email", "Address"]]
        for name, info in self.contacts.items():
            table.append([name, info['phone'], info['email'], info['address']])

        print(tabulate(tabular_data=table, headers="firstrow", tablefmt="pretty"))

    def update_contact(self, name, phone=None, email=None, address=None):
        if name not in self.contacts:
            rprint("[red bold]Contact not found!")
        else:
            if phone:
                self.contacts[name]['phone'] = phone

            if email:
                self.contacts[name]['email'] = email

            if address:
                self.contacts[name]['address'] = address

            rprint("[red bold]Conract Updated!")

    def delete_contact(self, name):
            if name in self.contacts:
                del self.contacts[name]
                rprint("[red bold]Contact Deleted!")
            else:
                rprint("[red bold]Contact not found!")

# TODO: add search method
