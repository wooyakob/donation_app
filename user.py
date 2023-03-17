# Login Function
def login(database, username, password):
    username = username.lower() # Convert username to lowercase
    if username in database:
        if database[username] == password:
            print("\n")
            print("Welcome to DonateMe " + username.title() + "!")
            return username.title() # Return with title case
        else: 
            print("\n")
            print("Incorrect password for user " + username.title())
            return ""
    else:
        print("Username " + username.title() + " not found in database")
        return ""


# Register Function
def register(database):
    while True:
        username = input("Please enter your desired username (1-10 characters): ").strip()
        if len(username) >= 1 and len(username) <= 10:
            break
        else:
            print("Error! Username must be between 1-10 characters.")
    while True:
        password = input("Please enter your desired password (1-4 characters): ").strip()
        if len(password) >= 1 and len(password) <= 4:
            break
        else:
            print("Error! Password must be between 1-4 characters.")
    if username.upper() in database:
        print("Username already exists.")
        return ""
    else:
        database[username.upper()] = password
        print("Your new username has been registered.")
        return username.upper()

# Donate Function
def donate(authorized_user, donations_list):
    # Check if user is logged in
    if authorized_user == "":
        print("You are not logged in")
    else:
        # Get donation amount from user and validate input
        while True:
            try:
                amount = float(input("Enter donation amount: $"))
                if amount <= 0:
                    raise ValueError("Invalid amount entered. Please enter a positive number.")
                break
            except ValueError as e:
                print(e)
        # Store donation
        donation_string = f"{authorized_user} donated ${amount}"
        donations_list.append(donation_string)
        print("Thank you for your donation!")
        print("")
    return donations_list