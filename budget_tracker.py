entries = []

def get_amount():
    """Ask for a valid positive amount."""
    while True:
        try:
            amount = float(input("Amount: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            return amount
        except ValueError:
            print("That is not a valid number. Please try again.")

def get_category():
    """Accept only income or expense."""
    while True:
        category = input("Category (income/expense): ").strip().lower()
        if category in ("income", "expense"):
            return category
        print("Invalid category. Enter income or expense.")

def add_entry():
    """Collect and store a transaction."""
    description = input("Description: ").strip()
    if not description:
        print("Description cannot be empty.")
        return

    amount = get_amount()
    category = get_category()

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
    """Display all recorded transactions."""
    if not entries:
        print("No entries recorded yet.")
        return

    print("\n=== All Entries ===")
    for index, entry in enumerate(entries, start=1):
        print(f"\nEntry {index}")
        print(f"Description: {entry['description']}")
        print(f"Amount: {entry['amount']:.2f}")
        print(f"Category: {entry['category']}")

def calculate_total():
    """Calculate and display the current balance."""
    total = 0
    for entry in entries:
        total += entry["amount"]
    print(f"Total balance: {total:.2f}")

def main():
    """Run the budget tracker menu."""
    while True:
        print("\n=== Budget Tracker ===")
        print("1. Add entry")
        print("2. View all entries")
        print("3. View total balance")
        print("4. Quit")

        choice = input("Choose an option: ").strip()

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
            print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()