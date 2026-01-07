items = {}
while True:
    print("\nCommands:ADD <item_name> <price> <quantity>|BILL|EXIT")
    command = input("Enter command: ").lower().split()
    if command[0] == "add":
        item_name = command[1]
        price = float(command[2])
        quantity = int(command[3])
        if item_name in items:
            items[item_name]["quantity"] += quantity
        else:
            items[item_name] = {"price": price, "quantity": quantity}
        print(f"Added {item_name}")
    elif command[0] == "bill":
        if not items:
            print("No items added.")
            continue
        total = 0
        print("\nItem Wise Bill:")
        print("Item\tPrice\tQty\tAmount")
        for item, data in items.items():
            amount = data["price"] * data["quantity"]
            total += amount
            print(f"{item}\t{data['price']}\t{data['quantity']}\t{amount}")
        discount = 0
        if total >= 1000:
            discount = total * 0.10
        final_amount = total - discount
        print(f"\nTotal Amount: ₹{total}")
        print(f"Discount: ₹{discount}")
        print(f"Final Payable Amount: ₹{final_amount}")
    elif command[0] == "exit":
        print("Exiting Grocery Billing System.")
        break
    else:
        print("Invalid command. Try again.")
