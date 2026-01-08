from tabulate import tabulate
from rich import print as rprint


class ContactBook:
    """This class is for the features of a contact book (CRUD Operations)
    """
    def __init__(self):
        self.contacts = {}

    def add_contact(
            self, name: str, phone: str,
            email: str = "", address: str = ""
    ) -> None:
        """This method adds a new contact to the list of contacts.

        :param name: Name of the contact.
        :param phone: The phone number of the contact
        :param email: The email address of the contact, defaults to None
        :param address: The physical address of the contatc, defaults to None
        """
        if name not in self.contacts:
            self.contacts[name] = {
                "phone": phone,
                "email": email,
                "address": address
            }
            rprint("[red bold]Contact Created.")
            
        else:
            rprint("[red bold]Contact Already Exists!")

    def list_contacts(self) -> None:
        """This method lists all the contacts in a table.
        """
        rprint("\n\n[blue bold]List of Contacts:")
        table = [["Name", "Phone Number", "Email", "Address"]]
        for name, info in self.contacts.items():
            table.append([name, info['phone'], info['email'], info['address']])

        print(tabulate(tabular_data=table, headers="firstrow", tablefmt="pretty"))

    def update_contact(
            self, name: str, phone: str = "",
            email: str = "", address: str = ""
    ) -> None:
        """This method updates a contact.

        :param name: Name of the contact
        :param phone: The new phone number of the contact, defaults to None
        :param email: The new email address of the contact, defaults to None
        :param address: The new physical address of the contact, defaults to None
        """
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

    def delete_contact(self, name: str) -> None:
        """This method deletes the contact.

        :param name: Name of the contact you want to delete
        """
        if name in self.contacts:
            warning = input(f"Are you sure about deleting {name}'s contact? (y/n)")
            if warning == "y":
                del self.contacts[name]
                rprint("[red bold]Contact Deleted!")
                
        else:
            rprint("[red bold]Contact not found!")
# TODO: add search method
