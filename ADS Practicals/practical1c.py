class CircularQueue:

    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.capacity = capacity
        self.front = -1
        self.rear = -1
        self.count = 0

    # Enqueue operation
    def enqueue(self, item):
        if self.is_full():
            print("Queue Overflow! Queue is full")
            return

        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity

        self.queue[self.rear] = item
        self.count += 1

        print(item, "enqueued into queue")

    # Dequeue operation
    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow! Queue is empty")
            return

        item = self.queue[self.front]

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity

        self.count -= 1

        print(item, "dequeued from queue")

    # Peek operation
    def peek(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Front element:", self.queue[self.front])

    # Check if queue is empty
    def is_empty(self):
        return self.front == -1

    # Check if queue is full
    def is_full(self):
        return self.count == self.capacity

    # Return size
    def size(self):
        return self.count

    # Display queue
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return

        print("Queue elements:")

        i = self.front

        while True:
            print(self.queue[i], end=" ")

            if i == self.rear:
                break

            i = (i + 1) % self.capacity

        print()


# Driver Program

capacity = int(input("Enter queue capacity: "))
q = CircularQueue(capacity)

while True:

    print("\nName: Almash Lakdawala")
    print("Enrollment: 26PG030052")

    print("\n--- Circular Queue Menu ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Check if Empty")
    print("5. Check if Full")
    print("6. Size")
    print("7. Display")
    print("8. Exit")

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
        print("Queue is Full" if q.is_full() else "Queue is Not Full")

    elif choice == 6:
        print("Queue Size:", q.size())

    elif choice == 7:
        q.display()

    elif choice == 8:
        print("Exiting...")
        break

    else:
        print("Invalid Choice!")