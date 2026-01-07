available_slots = [1, 2]   
parking = {}
while True:
    print("\nCommands:park <vehicle_no> | remove <vehicle_no> | status | exit")
    command = input("Enter command: ").split()
    if command[0] == "park":
        vehicle_no = command[1]
        if not available_slots:
            print("Parking full.")
        else:
            slot = available_slots.pop(0)
            parking[slot] = vehicle_no
            print("Vehicle ",vehicle_no," parked at slot ",slot)
    elif command[0] == "remove":
        vehicle_no = command[1]
        found = False
        for slot, vehicle in parking.items():
            if vehicle == vehicle_no:
                del parking[slot]
                available_slots.append(slot)
                available_slots.sort()
                print(f"Vehicle {vehicle_no} removed from slot {slot}")
                found = True
                break
        if not found:
            print("Vehicle not found.")
    elif command[0] == "status":
        print(f"Available slots count: {len(available_slots)}")
    elif command[0] == "exit":
        print("Exiting Parking Slot Management System.")
        break
    else:
        print("Invalid command. Try again.")
