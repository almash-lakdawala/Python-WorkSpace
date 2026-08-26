# Queue Implementation Using Array in Python

queue = []
MAX_SIZE = 5


# Enqueue operation
def enqueue():
    if len(queue) == MAX_SIZE:
        print("Queue Overflow! Queue is full.")
    else:
        value = int(input("Enter value to insert: "))
        queue.append(value)
        print(value, "inserted into queue.")


# Dequeue operation
def dequeue():
    if len(queue) == 0:
        print("Queue Underflow! Queue is empty.")
    else:
        value = queue.pop(0)
        print(value, "deleted from queue.")


# Peek operation
def peek():
    if len(queue) == 0:
        print("Queue is empty.")
    else:
        print("Front element is:", queue[0])


# Display operation
def display():
    if len(queue) == 0:
        print("Queue is empty.")
    else:
        print("Queue elements are:")
        for element in queue:
            print(element, end=" ")
        print()


# Main program
while True:
    print("\n----- QUEUE MENU -----")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        enqueue()

    elif choice == 2:
        dequeue()

    elif choice == 3:
        peek()

    elif choice == 4:
        display()

    elif choice == 5:
        print("Program terminated.")
        break

    else:
        print("Invalid choice! Please try again.")