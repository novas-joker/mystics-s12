rooms = [1,2]
while True:
    print("\nCommands: ALLOCATE | STATUS | EXIT")
    command = input("Enter command: ").lower()
    if command == "allocate":
        if len(rooms) == 0:
            print("No rooms available.")
        else:
            student_id = input("Enter Student ID: ")
            room_assigned = rooms.pop(0)
            print("Room allocated to",student_id," :Room",room_assigned )
    elif command == "status":
        print("Available rooms : ",len(rooms))
    elif command == "exit":
        print("Exiting Hostel Room Allocation System.")
        break
    else:
        print("Invalid command. Please try again.")
