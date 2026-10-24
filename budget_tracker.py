entries = []

def get_amount():
    while True:
        try:
            amount = float(input("Amount: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            return amount
        except ValueError:
            print("That is not a valid number. Please try again.")

def add_entry():
    description = input("Description: ")
    amount = get_amount()
    category = input("Category (income/expense): ").lower()

    if category == "expense":
        amount = -amount

    entry = {
        "description": description,
        "amount": amount,
        "category": category
    }

    entries.append(entry)
    print("Entry added.")

def view_entries():
    if not entries:
        print("No entries recorded yet.")
        return

    print("\n=== All Entriesm ===")
    for index, entry in enumerate(entries, start=1):
        print(f"\nEntry {index}")
        print(f"Description: {entry['description']}")
        print(f"Amount: {entry['amount']: .2f}")
        print(f"Category: {entry['category']}")

def calculate_total():
    total = 0
    for entry in entries:
        total += entry["amount"]
    print(f"Total balance: {total: .2f}")    

print("=== Budget Tracker ===")

while True:
    print("\n1. Add entry")
    print("2. View all entries")
    print("3. View total balance")
    print("4. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_entry()
    elif choice == "2":
        view_entries()
    elif choice == "3":
        calculate_total()        
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("invalid choice. Please select 1,2,3, or 4")