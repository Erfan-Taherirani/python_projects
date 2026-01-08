![Banner](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTBPcUuZHawj6vqG8_JXdEPI9ZO2_gPIFodnw&s)

# Introduction
Contact Book is a command-line application that demonstrates CRUD (Create, Read, Update, Delete) operations for managing contacts. Users can add new contacts, view all stored contacts, update existing contact information, and delete contacts from the system.

>**Note**: This is a practice project focused on implementing CRUD operations. Currently, contacts are stored in memory only and are not persisted to a database or file. Data will be lost when the application closes. Persistent storage functionality is planned for future updates.

## Features
- `add_contact`: Create new contacts with name, phone number, email, and address

- `list_contacts`: Display all saved contacts in an organized format

- `update_contact`: Modify information for existing contacts

- `delete_contact`: Remove unwanted contacts from the system

`User-Friendly Interface` - Simple command-line menu for easy navigation

## Requirements
- **Python 3.12** or higher

- Third-party Python packages:

    - `tabulate==0.9.0` - For formatted table display
    - `rich==14.2.0` - For enhanced terminal output



**Operating System**: Compatible with Windows, macOS, and Linux

>**Note**: All dependencies can be installed via the requirements.txt file (see Installation section).

## Installation
1. Clone the Repository:
```bash
git clone https://github.com/Erfan-Taherirani/python_projects.git
```

2. Navigate to the Project:
```bash
cd "Contact Book"
```

3. Create a Virtual Environment:
```bash
conda create -n cbook_env
```

4. Activate the Virtual Environment:
```bash
conda activate cbook_env
```

5. Install Required Dependencies:
```bash
pip install -r requirements.txt
```

## Usage
Starting the Application
Run the application using:

```bash
python src/main.py
```
```
### Main Menu

Upon launching, you'll see a menu with the following options:
~~~
1. Add Contact
2. List Contacts
3. Update Contact
4. Delete Contact
5. Quit
```
Select an option by entering the corresponding number and pressing Enter.
Features Guide
1. **Add Contact**

- Select option `1` from the main menu
- Enter the contact details when prompted:
    - Name
    - Phone Number
    - Email
    - Address


- The contact will be added to your contact list

2. **List Contacts**

- Select option `2` from the main menu
- All contacts will be displayed in a formatted table with columns: Name, Phone Number, Email, and Address

3. **Update Contact**

- Select option `3` from the main menu
- Enter the name of the contact you want to update
Update the following fields as needed:
    - Phone Number
    - Email
    - Address


>**Note**: Press Enter to keep the current value unchanged, or press Space then Enter to clear a field

4. **Delete Contact**

- Select option `4` from the main menu
- Enter the name of the contact you want to delete
- Confirm the deletion when prompted
- The contact will be permanently removed from the list

5. **Quit**

- Select option 5 to exit the application
- All data will be lost upon exit (contacts are not saved)

## Project Structure
```
Contact Book/
│
├── src/
│   ├── utils/
│   │   └── contact_book.py    # Core contact management logic
│   │
│   └── main.py                # Application entry point
│
├── README.md                  # Project documentation
└── requirements.txt           # Python dependencies
```
**File Descriptions**

- `src/main.py` - Entry point of the application, handles the user interface and menu system
- `src/utils/contact_book.py` - Contains the main ContactBook class and CRUD operation functions (add, list, update, delete contacts)
- `README.md` - Project documentation and usage instructions
- `requirements.txt` - Lists all required third-party Python packages (tabulate, rich)

## Contact Info
**Author:** Erfan Taherirani

For questions, feedback, or collaboration opportunities, feel free to reach out:

- **GitHub:** github.com/Erfan-Taherirani
- **Gmail:** e.taherirani81@gmail.com
- **LinkedIn:** linkedin.com/in/erfan-taherirani
- **Telegram:** t.me/WWW_ErfanT_ir

Contributions, suggestions, and bug reports are welcome. Please feel free to open an issue or submit a pull request on the GitHub repository.
