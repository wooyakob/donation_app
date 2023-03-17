# Import My Function
from donations_pkg.homepage import show_homepage, show_donations
from donations_pkg.user import login, register, donate

# Dictionary, List & String Data Types
database = {"admin": "password123", "ADMIN": "password123"}
donations = []
authorized_user = ""
donations_list = []

# Menu Display
show_homepage()
while True:
    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print("\n")
        print("Logged in as: " + authorized_user)

    # User Options Logic
    print("\n")
    user_option = input("Choose an option: 1, 2, 3, 4, or 5: ")

    if user_option == '1':
        print("\n")
        username = input("Please enter your username: ").upper()
        password = input("Please enter your password: ")
        authorized_user = login(database, username, password)
    elif user_option == '2':
        username = input("Please enter a new username between 1-10 characters: ")
        password = input("Please enter a new password between 1-4 digits: ")
        if authorized_user != "":
            database[username] = password
            print(f"Added user {username} with password {password} to the database.")
    elif user_option == '3':
        if authorized_user == "":
            print("You are not logged in")
        else:
            try:
                amount = float(input("Enter donation amount: $"))
                donation_string = f"{authorized_user} donated ${amount}"
                donations_list.append(donation_string)
                print("Thank you for your donation!")
            except ValueError:
                print("Invalid amount entered. Please try again.")
    elif user_option == '4':
        show_donations(donations_list)
    elif user_option == '5':
        print("Leaving DonateMe...")
        break
    else:
        print("Invalid option. Please choose a valid option.")
