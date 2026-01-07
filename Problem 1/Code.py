from collections import deque
size = 100
queue = deque()
token_counter = 1
while True:
    print("\nCommands: ADD | SERVE | STATUS | EXIT")
    command = input("Enter command: ").lower()
    if command == "add":
        if len(queue) == size:
            print("Queue is full. Cannot add more students.")
        else:
            queue.append(token_counter)
            print("Token generated: ",token_counter)
            token_counter += 1
    elif command == "serve":
        if len(queue) == 0:
            print("No students to serve.")
        else:
            served_token = queue.popleft()
            print("Serving token:",served_token)
    elif command == "status":
        print("Students waiting in queue:",len(queue))
    elif command == "exit":
        print("Exiting Canteen Queue Management System.")
        break
    else:
        print("Invalid command. Please try again.")
