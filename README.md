# Phonebook CLI Application

## Install
1. To run this program you need Python 3.6 installed and this program is made for Unix terminals.
2. Install the requirements for the program to run (specially termcolor)
```
pip3 install -r requirements.txt
```

## Running the program
2. Inside program directory, run the code:
```
python3 phonebook.py
```

## Features
1. Add contacts:
Saves name, phone number, address, email and notes about the contact.

2. Edit contacts:
Edit all info about the contact besides the name (it can delete de contact though).

3. List contacts:
List all contact names saved in the database.

4. Search contacts:
It searches the database for all contacts that match the string searched. (It's not case sensitive).
E.g: if you have John and James in your contacts and your search for 'j' it will show both contacts.

5. Delete contacts:
Deletes a contact based on the name given.

6. Saves the contacts in a exterior file inside the program folder. Auto saves the contacts and loads it automatically when program is run or exit.
