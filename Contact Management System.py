#Question 1
import re

def main():

    contacts = {}

    def add_contact(contacts, name, number, email, details):

        while not re.match(r"^[a-zA-Z\s]+$", name):
            name = input("Invalid name. Please enter again: ")

        while not re.match(r"^\+?\d{1,3}\s?\(?\d{1,3}\)?[\s.-]?\d{3,4}[\s.-]?\d{4}$", number):
            number = input("Invalid phone number. Please enter again: ")

        if email and not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            email = input("Invalid email address. Please enter again (or leave blank): ")

        contacts[name] = {'Number': number, 'Email': email, 'Details': details}
        
        print("Contact added successfully.")

    def edit_contact(contacts, name, new_number=None, new_email=None):

        name = input("Enter the name of the contact to edit: ")

        if name in contacts:
            print("Contact found. Choose a field to edit:")
            print("1. Phone Number")
            print("2. Email")
            print("3. Details")

            choice = input("Please choose a selection(1/2/3): ")

            if choice == '1':
                new_number = input("Please enter new phone number: ")
                while not re.match(r"^\d{10}$", new_number):
                    new_number = input("Invalid phone number. Please enter a 10-digit number: ")
                contacts[name]["phone"] = new_number
                print("Phone number updated successfully!")

            elif choice == '2':
                new_email = input("Enter the new email address: ")
                while not re.match(r"[^@]+@[^@]+\.[^@]+", new_email):
                    new_email = input("Invalid email address. Please enter a valid email: ")
                contacts[name]["email"] = new_email
                print("Email address updated successfully!")

            elif choice == '3':
                new_details = input("Please enter new details: ")
                contacts[name]["details"] = new_details
                print("Additional details updated!")

            else:
                print("Invalid choice.")

        else:
            print("Contact does not exist.")

    def delete_contact():
        while True:
            if not name:
                print("Name cannot be empty. Please try again.")

            matches = []
            for key in contacts:
                if re.search(name, key, re.IGNORECASE):
                    matches.append(key)

            if not matches:
                print("No contacts found matching that name.")
            elif len(matches) == 1:
                del contacts[matches[0]]
                print("Contact deleted successfully.")
                break

            print("Multiple matches found:")
            if 1 <= choice <= len(matches):
                del contacts[matches[choice-1]]
                print("Contact deleted successfully.")
                break
            else:
                print("Invalid choice. Please try again.")

    def search_contact(contacts, search):
        results = []
        for contact_name, data in contacts.items():
            if search == contact_name:
                results.append((contact_name, data))
        return results

    def print_search_results(results):
        if results:
            for (contact_name, data) in results:
                print(f"Name: {contact_name}")
                print("-" * 20)
                for key, value in data.items():
                    print(f"{key}: {value}")
                print("-" * 20)
        else:
            print("No matching contacts found.")

    def display_contacts(contacts):
        try:
            if len(contacts) == 0:
                print("--No contacts to display!!--")
            for key, value in contacts.items():
                print(key, ":", value)
        except TypeError:
            print("--No contacts to display!!--")

    def export_contacts(contacts, filename="contacts.txt"):
        if not contacts:
            print("--No contacts to export!!--")
        
        with open(filename, "w", encoding="utf-8") as file:
            for name, details in contacts.items():
                contact_string = f"{name}: {details}\n"
                file.write(contact_string)
                print("--Contact exported!!--")
            
    def import_contacts(filename="contacts.txt"):
        imported_contacts = {}
        try:
            with open('contacts.txt', 'r', encoding="utf-8") as file:
                for line in file:
                    name, details = line.strip().split(',', 1)
                    contacts[name] = details
            print("--Contacts Imported!!--")
            print(imported_contacts)
        except FileNotFoundError:
            print(" --No Text File Not Found!!-- ")

    while True:
        print("Welcome to the Contact Management System!!")
        print("Menu:")
        print("1. Add a New Contact")
        print("2. Edit an Existing Contact")
        print("3. Delete a Contact")
        print("4. Search for a Contact")
        print("5. Display all Contacts")
        print("6. Export Contacts to a Text File")
        print("7. Import Contacts from a Text File *BONUS*")
        print("8. Quit")

        choice = input("Please select an option: ")

        if choice == '1':
            name = input("Enter contact name: ")
            number = input("Enter phone number: ")
            email = input("Enter email address (optional): ")
            details = input("Enter additional details (optional): ")
            add_contact(contacts, name, number, email, details)
        elif choice == '2':
            edit_contact(contacts, name, new_number=None, new_email=None)
        elif choice == '3':
            name = input("Enter the name of the contact to delete: ")
            delete_contact()
        elif choice == '4':
            search = input("Please enter contact: ")
            results = search_contact(contacts, search)
            print_search_results(results)
        elif choice == '5':
            display_contacts(contacts)
        elif choice == '6':
            export_contacts(contacts, filename="contacts.txt")
        elif choice == '7':
            import_contacts(filename="contacts,txt")
        elif choice == '8':
            print("Thank you for using the Contact Management System!!")
            break
        else:
            print("Not a valid choice. Please Try Again.")

if __name__ == "__main__":
    main()