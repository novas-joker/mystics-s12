rooms = [1, 2]
students = []
while True:
    print("\nCommands: ALLOCATE | STATUS | EXIT")
    command = input("Enter command: ").lower()
    if command == "allocate":
        if len(rooms) == 0:
            print("No rooms available.")
        else:
            student_id = input("Enter Student ID: ")
            if student_id not in students:
                students.append(student_id)
                room_assigned = rooms.pop(0)
                print(f"Room allocated to {student_id}: Room {room_assigned}")
            else:
                print("Student already exists.")
    elif command == "status":
        print(f"Available rooms: {len(rooms)}")
        print("Allocated rooms:")
        for i, student in enumerate(students):
            print(f"Room {i+1}: {student}")
    elif command == "exit":
        print("Exiting Hostel Room Allocation System.")
        break
    else:
        print("Invalid command. Please try again.")

