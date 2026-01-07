print("Password Strength Checker")
print("-------------------------")
print("Commands: check <password> | exit")
rules = [
    lambda s: len(s) >= 8,  
    lambda s: any(c.isupper() for c in s),  
    lambda s: any(c.islower() for c in s),  
    lambda s: any(c.isdigit() for c in s),  
    lambda s: any(not c.isalnum() for c in s),  
]
while True:
    try:
        command = input("Enter command: ").lower().split()
        if command[0] == "check":
            if len(command) != 2:
                print("Invalid command. Usage: check <password>")
                continue
            password = command[1]
            strength = sum(rule(password) for rule in rules)
            if strength == 5:
                print(f"Password strength: Strong")
            elif strength >= 3:
                print(f"Password strength: Medium")
            else:
                print(f"Password strength: Weak")
        elif command[0] == "exit":
            print("Exiting Password Strength Checker.")
            break
        else:
            print("Invalid command. Try again.")
    except IndexError:
        print("Invalid command. Please provide a password.")
    except KeyboardInterrupt:
        print("\nExiting Password Strength Checker.")
        break
    except Exception as e:
        print(f"An error occurred: {e}")

