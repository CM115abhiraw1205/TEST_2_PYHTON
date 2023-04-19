phoneDirectory = {}
print()
print("WELCOME TO THE GRANN'S PHONE DIRECTORY")

while True:
    print()
    print("1. Add a record")
    print("2. Search a record")
    print("3. Update a record")
    print("4. Delete a record")
    print("5. Quit")
    print()
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter your 10-digit phone number: ")
        phoneDirectory[name] = phone
        print("Record added successfully")

    elif choice == '2':
        name = input("Enter name to search: ")
        if name in phoneDirectory:
            print(name + ":" + phoneDirectory[name])
        else:
            print("Record not found")

    elif choice == '3':
        name = input("Enter name to update: ")
        if name in phoneDirectory:
            phone = input("Enter new 10-digit phone number: ")
            phoneDirectory[name] = phone
            print("Record updated successfully")
        else:
            print("Record not found")

    elif choice == '4':
        name = input("Enter name to delete: ")
        if name in phoneDirectory:
            del phoneDirectory[name]
            print("Record deleted successfully")
        else:
            print("Record not found")

    elif choice == '5':
        print("Exiting program")
        break

    else:
        print("Invalid choice. Please enter a valid choice (1-5)")
