expenses = {}
while True:
    print("\nCommands: add <amount> <category> | report | exit")
    try:
        command = input("Enter command: ").lower().split()
        if command[0] == "add":
            if len(command) != 3:
                print("Invalid command. Usage: add <amount> <category>")
                continue
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
                max_expense = max(expenses.values())
                highest_categories = [cat for cat, amt in expenses.items() if amt == max_expense]
                print("Total Expenses:", total)
                for cat, amt in expenses.items():
                    print(cat, ":", amt)
                if len(highest_categories) > 1:
                    print("Highest Spending Categories:", ', '.join(highest_categories))
                else:
                    print("Highest Spending Category:", highest_categories[0])
        elif command[0] == "exit":
            print("Exiting Monthly Expense Tracker.")
            break
        else:
            print("Invalid command. Try again.")
    except IndexError:
        print("Invalid command. Please provide amount and category.")
    except ValueError:
        print("Invalid input. Please check amount.")
    except KeyboardInterrupt:
        print("\nExiting Monthly Expense Tracker.")
        break
    except Exception as e:
        print(f"An error occurred: {e}")
