class ContactBook:
    def __init__(self):
        self.contacts = {}
        self.names = []

    def create(self, name:str, email, phone_number, physical_address):
        if name not in self.names:
            self.names.append(name)

        self.contacts.setdefault(name, {"email": email,
                                      "phone number": phone_number,
                                      "physical address": physical_address}
        )
        print("New Contact created.")

    def show(self):
            for name in self.names:
                print(name)
                print(f"    Email: {self.contacts[name]['email']}")
                print(f"    Phone Number: {self.contacts[name]['phone number']}")
                print(f"    Physical Address: {self.contacts[name]['physical address']}")
                print("---------------------------------")

    def edit(self, name, new_name, email, phone_number, physical_address):
        if name in self.names:
            if name == new_name:
                self.contacts.update({name: {"email": email,
                                        "phone number": phone_number,
                                        "physical address": physical_address}}
                )
            else:
                self.contacts.pop(name)
                self.contacts.update({new_name: {"email": email,
                                        "phone number": phone_number,
                                        "physical address": physical_address}}
                )
                self.names.remove(name)
                self.names.append(new_name)
                
            print(f"{name}'s Contact Edited.")
        else:
            print("This contact doesn't exist.")

    def delete(self, name):
        if name in self.names:
            self.contacts.pop(name)
            self.names.remove(name)
            print("Contact Deleted.")
        else:
            print("This contact doesn't exist.")

    def search(self, name):
        if name in self.names:
            print(name)
            print(f"    Email: {self.contacts[name]['email']}")
            print(f"    Phone Number: {self.contacts[name]['phone number']}")
            print(f"    Physical Address: {self.contacts[name]['physical address']}")
            print("---------------------------------")
        else:
            print(f"There is no {name}")
