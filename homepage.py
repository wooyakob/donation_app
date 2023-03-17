def show_homepage():
    print("     === DonateMe Homepage ===")
    print("-------------------------------------")
    print("| 1. Login      | 2. Register       |")
    print("-------------------------------------")
    print("| 3. Donate     | 4. Show Donations |")
    print("-------------------------------------")
    print("|            5. Exit                |")
    print("-------------------------------------")

def show_donations(donations_list):
    total_donations = 0
    print("\nDonations:")
    for donation in donations_list:
        print(donation)
        donation_amt = float(donation.split('$')[1])
        total_donations += donation_amt
    print(f"\nTotal Donations: ${total_donations:.2f}")
