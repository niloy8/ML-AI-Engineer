from validate_email import validate_email
contacts = []

def add_contact():
    while True:
        name = input("Enter your name - " )
        if not any(char.isalpha() for char in name):
            print("It should be valid name")
        else:
            break
    while True:
        try:
            age =int(input("Enter your age- "))
            break

        except ValueError:
            print("Enter your valid age")


    while True:
        email = input("Enter your mail - ")
        if validate_email(email):
            break
        else:
            print("Enter a valid email")
    contact = {
        "name":name,
        "age": age,
        "email": email
    }
    contacts.append(contact)




def search_contacts():
    search = input("Enter the name you want to search - ")
    if contacts:
        for contact in contacts:
            if contact["name"].lower() == search.lower():
                print("Found")
                print(contact)
            else:
                print("Not Found")
                return
    else:
        print("No Account has been added yet plz add contact")


def show_contacts():
    if not contacts:
        print("No contacts found.")
        return
    for contcat  in contacts:
           print("------")
           print("Name:", contcat["name"])
           print("Age:", contcat["age"])
           print("Email:", contcat["email"])

def main_menu():
    print("*" *80)
    print("Contact Book Application")
    while True:
         print("\n1. Add Contact")
         print("2. View Contacts")
         print("3. Search Contact")
         print("4. Exit")

         while True:
             try:
                option = int(input("Enter your option - "))
                if option == 1:
                    add_contact()
                elif option == 2:
                    show_contacts()
                elif option == 3:
                    search_contacts()
                elif option == 4:
                    exit()
                else:
                    print("Invalid Option")

             except ValueError:
                print("Enter a valid option")
                break
if __name__ == "__main__":
    main_menu()
