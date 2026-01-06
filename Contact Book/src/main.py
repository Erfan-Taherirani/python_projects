from collections import defaultdict


class ContactBook:
    def __init__(self):
        self.contacts = defaultdict()

    def add_contact(self, name, phone, email, address):
        if name not in self.contacts:
            self.contacts[name] = {
                "phone": phone,
                "email": email,
                "address": address
            }
            
        else:
            print("Contact Already Exists!")

    def list_contacts(self):
        print("\n\nList of Contacts:")
        for name, info in self.contacts.items():
            print("-" * 20)
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print(f"Address: {info['address']}")
