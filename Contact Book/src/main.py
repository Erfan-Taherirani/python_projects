import utils.contact_book

if __name__ == "__main__":
    print("Welcome to the contact book application.")
    cbook = utils.contact_book.ContactBook()

    while True:
        print("\n1. Add Contact")
        print("2. List of Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Quit")

        user_input = input("Enter the feature number: ")

        if user_input == "5":
            break

        elif user_input == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            cbook.add_contact(
                name=name, phone=phone,
                email=email, address=address
            )

        elif user_input == "2":
            cbook.list_contacts()
            while True:
                contact_list_user_input = input(
                    "Press ok to continue\n"
                )
                if contact_list_user_input.lower() == "ok":
                    break
                else:
                    pass
