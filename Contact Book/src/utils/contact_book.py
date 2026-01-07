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
            print("Contact Created.")
            
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

    def update_contact(self, name, phone=None, email=None, address=None):
        if name in self.contacts:
            if phone or (phone == ""):
                self.contacts[name]['phone'] = phone
                print("Phone Updated!")

            if email or (email == ""):
                self.contacts[name]['email'] = email
                print("Email Updated!")

            if address or (address == ""):
                self.contacts[name]['address'] = address
                print("Address Updated!")

        else:
            print("Contact not found!")

    def delete_contact(self, name):
            del self.contacts[name]
            print("Contact Deleted!")
