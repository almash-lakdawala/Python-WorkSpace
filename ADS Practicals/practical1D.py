# Queue Implementation Using Linked List in Python

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Queue class
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Enqueue operation
    def enqueue(self, data):
        new_node = Node(data)

        # If queue is empty
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        print(data, "inserted into queue.")

    # Dequeue operation
    def dequeue(self):
        if self.front is None:
            print("Queue Underflow! Queue is empty.")
            return

        temp = self.front
        self.front = self.front.next

        # If queue becomes empty
        if self.front is None:
            self.rear = None

        print(temp.data, "deleted from queue.")

    # Peek operation
    def peek(self):
        if self.front is None:
            print("Queue is empty.")
        else:
            print("Front element is:", self.front.data)

    # Display operation
    def display(self):
        if self.front is None:
            print("Queue is empty.")
            return

        temp = self.front

        print("Queue elements are:")
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next

        print()


# Main program
queue = Queue()

while True:
    print("\n----- QUEUE USING LINKED LIST -----")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value to insert: "))
        queue.enqueue(value)

    elif choice == 2:
        queue.dequeue()

    elif choice == 3:
        queue.peek()

    elif choice == 4:
        queue.display()

    elif choice == 5:
        print("Program terminated.")
        break

    else:
        print("Invalid choice! Please try again.")