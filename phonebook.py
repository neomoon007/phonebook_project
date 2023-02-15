# Phonebook Application by Marcos Costa

# Imports
import os # Use Linux terminal commands
import pickle # Save and Load external files
from termcolor import colored # Use colors

# Create a function that saves the phonebook to a file
def save_phonebook(phonebook):
    with open("phonebook.pickle", "wb") as f:
        pickle.dump(phonebook, f)

# Create a function that loads the phonebook from a file
def load_phonebook():
    try:
        with open("phonebook.pickle", "rb") as f:
            phonebook = pickle.load(f)
            return phonebook
    except FileNotFoundError:
        return {}

# Initiate the variable that's gonna save the contacts
phonebook = load_phonebook()

# Create a function that saves the contact's info
def add_contact(name="", phone_number="", address="", email="", notes=""):
   
    # Header
    screen_update()
    header_format("CONTACT INFO", "blue")
    print(colored("\n" + "(*) - optional" + "\n", "yellow"))

    if name is "":
        name = input(colored("Name: ", "yellow")).title()
    
    # Check it's a valid name
    if name.isalpha() and len(name) > 0:
        
        # If no phone number was given, the program asks for a valid brasilian phone number
        if phone_number is "":
            phone_number = input(colored("Phone Number: ", "yellow"))
        
        # Check if the phone_number given is a valid one (contains only digits and has 11 digits)
        if phone_number.isdigit() and len(phone_number) == 11:
            if address is "":
                address = input(colored("Address: (*) ", "yellow"))

            if email is "":
                email = input(colored("Email: (*) ", "yellow"))
    
            if notes is "":
                print(colored("Notes: (*) ", "yellow"))
                notes = input()

            phonebook[name] = (phone_number, address, email, notes)
            print(colored(name + " has been added to the phonebook.", "green"))
        else:
            print(colored("ERROR: Invalid phone number. Please enter a valid 11 digit phone number.", "red"))
            if input(colored("Would you like to try again? (*) ", "yellow")) == "yes":
                add_contact(name)
    else:
        print(colored("ERROR: Invalid name. Please enter a name with only alphabetical characters.", "red"))

    if input(colored("Would you like to add another contact? (*) ", "yellow")) == "yes":
        add_contact()

# Create a function that searches a contact
def search_contact(phonebook, search_string=""):
    if search_string is "":
        search_string = input(colored("Search contact: ", "yellow"))
    if search_string is "":
        print(colored("ERROR: Invalid name, please input a valid name.", "red"))
        return search_contact()   
    search_string.lower() # Ignore case sensitivity

    # Header
    screen_update()
    header_format("SEARCH RESULTS FOR: " + search_string.upper(), "blue")

    # Search for all contact's that have the string given
    results = [(name, phonebook[name][0], phonebook[name][1], phonebook[name][2], phonebook[name][3]) for name in phonebook if search_string in name.lower()]
    
    if results:
        for index, result in enumerate(results):
            print("-" * 60)
            print(colored("Name: ", "yellow") + str(result[0]))
            print(colored("Phone Number: ", "yellow") + str(result[1]))
            print(colored("Address: ", "yellow") + str(result[2]))
            print(colored("Email: ", "yellow") + str(result[3]))
            print(colored("Notes: ", "yellow"))
            print(str(result[4]))
        
    else:
        user_input = input(colored("No results found.", "red"))
        if user_input == "yes":
            add_contact(name)
        
# Create a function that deletes the selected contact
def remove_contact(name=""):
    if name is "":
        name = input(colored("Delete contact: ", "yellow"))
    if name is "":
        print(colored("ERROR: Invalid name, please input a valid name.", "red"))
        return remove_contact()

    if name in phonebook:
        del phonebook[name]
        print(colored(name + " has been removed from the phonebook.", "green"))
    else:
        print(colored(name + " not found in the phonebook.", "yellow"))

# Create a function to edit a existing contact
def edit_contact(name=""):

    if name is "":
        name = input(colored("Contact to edit: ", "yellow"))
    if name is "":
        print(colored("ERROR: Invalid name, please input a valid name.", "red"))
        return edit_contact()

    # Header
    screen_update()
    header_format(name.upper(), "blue")
    print(colored("\n" + "(*)          - Optional", "yellow"))
    print(colored("[ ]          - Old info", "yellow"))
    print(colored("delete notes - Type 'delete notes' on the notes field to clear it" + "\n", "yellow"))

    if name in phonebook:

        old_phone_number = phonebook[name][0]
        new_phone_number = input(colored("Phone Number: " + "[" + old_phone_number + "]" + " (*) ","yellow"))

        if new_phone_number == "":
            phonebook[name] = list(phonebook[name])
            phonebook[name][0] = old_phone_number
            phonebook[name] = tuple(phonebook[name])
        else:
            phonebook[name] = list(phonebook[name])
            phonebook[name][0] = new_phone_number
            phonebook[name] = tuple(phonebook[name])

        old_address = phonebook[name][1]
        new_address = input(colored("Address: " + "[" + old_address + "]" + " (*) ","yellow"))

        if new_address == "":
            phonebook[name] = list(phonebook[name])
            phonebook[name][1] = old_address
            phonebook[name] = tuple(phonebook[name])
        else:
            phonebook[name] = list(phonebook[name])
            phonebook[name][1] = new_address
            phonebook[name] = tuple(phonebook[name])

        old_email = phonebook[name][2]
        new_email = input(colored("Email: " + "[" + old_email + "]" + " (*) ","yellow"))

        if new_email == "":
            phonebook[name] = list(phonebook[name])
            phonebook[name][2] = old_email
            phonebook[name] = tuple(phonebook[name])
        else:
            phonebook[name] = list(phonebook[name])
            phonebook[name][2] = new_email
            phonebook[name] = tuple(phonebook[name])

        existing_notes = phonebook[name][3]
        print(colored("Notes:", "yellow"))
        new_notes = input(colored("[" + existing_notes + "]" + " (*) ","yellow"))

        if new_notes == "":
            phonebook[name] = list(phonebook[name])
            phonebook[name][3] = existing_notes
            phonebook[name] = tuple(phonebook[name])

        elif new_notes == "delete notes":
            phonebook[name] = list(phonebook[name])
            phonebook[name][3] = ""
            phonebook[name] = tuple(phonebook[name])

        else:
            phonebook[name] = list(phonebook[name])
            phonebook[name][3] = existing_notes + "\n" + new_notes
            phonebook[name] = tuple(phonebook[name])

        print(colored(name + " edited successfully." + "\n", "green"))

    else:
        user_input = input(name + " not found in the phonebook, would you like to add " + name + " to the phonebook?" + colored(" (*) ", "yellow"))
        if user_input == "yes":
            add_contact(name)

        if input("\n" + "Would you like to edit another contact? (*) ") == "yes":
            edit_contact()


# Create a function that lists all contacts in the phonebook
def list_contacts():
    for name in phonebook.keys():
        print("- " + name)
    print(" ")

# Create a function that formats headers
def header_format(header_text, color="white", width=60):
    print(colored("=" * width, color))
    print(colored(header_text.center(width), color))
    print(colored("=" * width, color))

# Create a function that handles the commands the user can give
def menu_header(): 
    
    # Prints the program
    header_format("PHONEBOOK v2.0", "blue")
    print("\n")
    print(colored("Commands:", "yellow"))
    print("(add)    - Add a contact")
    print("(edit)   - Edit a contact")
    print("(list)   - List all contacts")
    print("(search) - Search a contact")
    print("(delete) - Delete a contact")
    print("(quit)   - Quit the program")
    print("\n")

# Create a function that updates the screen.
def screen_update():
    # Clears the terminal before printing the program interface
    os.system('clear' if os.name == 'posix' else 'cls')

# Create a function that is the Menu of the program.
def program_menu():
    while True:

        screen_update() # Clears the screen
        menu_header() # Set the header
        user_input = input(colored("What would you like to do? ", "yellow"))

        if user_input == "add":
            add_contact()
        elif user_input == "edit":
            edit_contact()
            input("Press [enter] to go back to main menu.")
        elif user_input == "list":
            list_contacts()
            input("Press [enter] to go back to main menu.")
        elif user_input == "search":
            search_contact(phonebook)
            input("Press [enter] to go back to main menu.")
        elif user_input == "delete":
            remove_contact()
            input("Press [enter] to go back to main menu.")
        elif user_input == "quit":
            save_phonebook(phonebook)
            break
program_menu()
