import json

# Load contacts from a file
try:
    with open("contacts.json", "r") as file:
        contacts = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    contacts = {}

def save_contacts():
    """Save contacts to a file"""
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    """Add a new contact"""
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    contacts[name] = {"phone": phone, "email": email}
    save_contacts()
    print(f"Contact {name} added successfully!")

def search_contact():
    """Search for a contact"""
    name = input("Enter Name to Search: ")
    if name in contacts:
        print(f"Name: {name}\nPhone: {contacts[name]['phone']}\nEmail: {contacts[name]['email']}")
    else:
        print("Contact not found!")

def update_contact():
    """Update an existing contact"""
    name = input("Enter Name to Update: ")
    if name in contacts:
        phone = input("Enter New Phone Number: ")
        email = input("Enter New Email: ")
        contacts[name] = {"phone": phone, "email": email}
        save_contacts()
        print(f"Contact {name} updated successfully!")
    else:
        print("Contact not found!")

def delete_contact():
    """Delete a contact"""
    name = input("Enter Name to Delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts()
        print(f"Contact {name} deleted successfully!")
    else:
        print("Contact not found!")

def list_contacts():
    """List all contacts"""
    if contacts:
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        print("No contacts found!")

def main():
    """Main function to run the contact book"""
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. List Contacts")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            list_contacts()
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose again.")

if __name__ == "__main__":
    main()
