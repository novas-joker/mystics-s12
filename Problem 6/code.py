password = input("Enter password: ")
rules_met = 0
if len(password) >= 8:
    rules_met += 1
if any(c.isupper() for c in password):
    rules_met += 1
if any(c.islower() for c in password):
    rules_met += 1
if any(c.isdigit() for c in password):
    rules_met += 1
if any(not c.isalnum() for c in password):
    rules_met += 1
if rules_met == 5:
    print("Strong")
elif rules_met >= 3:
    print("Medium")
else:
    print("Weak")
