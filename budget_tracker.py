entries = []

def add_entry():
    entry = {
        "description": "Salary",
        "amount": 150000,
        "category": "income"
    }
    entries.append(entry)
    print("Entry added.")

print("=== Budget Tracker ===")

while True:
    print("\n1. Add entry")
    print("2. View all entries")
    print("3. View total balance")
    print("4. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_entry()
    elif choice == "4":
        print("Goodbye!")
        break