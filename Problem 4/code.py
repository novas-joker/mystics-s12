expenses = {}
while True:
    print("\nCommands: add <amount> <category> | report | exit")
    command = input("Enter command: ").split()
    if command[0] == "add":
        amount = float(command[1])
        category = command[2]
        if category in expenses:
            expenses[category] += amount
        else:
            expenses[category] = amount
    elif command[0] == "report":
        if not expenses:
            print("No expenses recorded.")
        else:
            total = sum(expenses.values())
            highest_category = max(expenses, key=expenses.get)
            print("Total Expenses:",total)
            for cat, amt in expenses.items():
                print(cat,":",amt)
            print("Highest Spending Category:",highest_category)
    elif command[0] == "exit":
        print("Exiting Monthly Expense Tracker.")
        break
    else:
        print("Invalid command. Try again.")
