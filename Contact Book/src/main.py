import utils.contact_book
from rich import print as rprint


if __name__ == "__main__":
    rprint("[white on cyan bold]Welcome to the contact book application.")
    cbook = utils.contact_book.ContactBook()

    while True:
        rprint("[bold]\n1. Add Contact")
        rprint("[bold]2. List of Contacts")
        rprint("[bold]3. Update Contact")
        rprint("[bold]4. Delete Contact")
        rprint("[bold]5. Quit")

        user_input = input("\nEnter the feature number: ").strip()

        if user_input == "5":
            break

        elif user_input == "1":
            name = input("Enter name: ").strip()
            phone = input("Enter phone: ").strip()
            email = input("Enter email: ").strip()
            address = input("Enter address: ").strip()
            cbook.add_contact(
                name=name, phone=phone,
                email=email, address=address
            )

        elif user_input == "2":
            cbook.list_contacts()
            while True:
                print("-" * 20)
                contact_list_user_input = input(
                    "Press any key to continue\n"
                )
                break

        elif user_input == "3":
            print("-" * 20)
            print("Press enter if you don't want to change an element")
            print("Press space to empty an element")
            print("-" * 20)
            name = input("Enter Name: ").strip()
            phone = input("Enter Phone: ")
            email = input("Enter Email: ")
            address = input("Enter address: ")
            cbook.update_contact(
                name=name,
                phone=phone,
                email=email,
                address=address
            )

        elif user_input == "4":
            name = input("Enter Name: ").strip()
            cbook.delete_contact(name=name)
