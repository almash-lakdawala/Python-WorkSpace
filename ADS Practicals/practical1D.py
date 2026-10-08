class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:

    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    # Enqueue operation
    def enqueue(self, item):
        new_node = Node(item)

        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        self.count += 1
        print(item, "enqueued into queue")

    # Dequeue operation
    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow! Queue is empty")
            return

        item = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        self.count -= 1
        print(item, "dequeued from queue")

    # Peek operation
    def peek(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Front element:", self.front.data)

    # Check if queue is empty
    def is_empty(self):
        return self.front is None

    # Return queue size
    def size(self):
        return self.count

    # Display queue
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return

        print("Queue elements:")

        temp = self.front

        while temp:
            print(temp.data, end=" ")
            temp = temp.next

        print()


# Driver Program

q = Queue()

while True:

    print("\nName: Almash Lakdawala")
    print("Enrollment: 26PG030052")

    print("\n--- Linked List Queue Menu ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Check if Empty")
    print("5. Size")
    print("6. Display")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = int(input("Enter element: "))
        q.enqueue(item)

    elif choice == 2:
        q.dequeue()

    elif choice == 3:
        q.peek()

    elif choice == 4:
        print("Queue is Empty" if q.is_empty() else "Queue is Not Empty")

    elif choice == 5:
        print("Queue Size:", q.size())

    elif choice == 6:
        q.display()

    elif choice == 7:
        print("Exiting...")
        break

    else:
        print("Invalid Choice!")