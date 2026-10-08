class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.top = None
        self.count = 0

    # Push operation
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self.count += 1
        print(item, "pushed into stack")

    # Pop operation
    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Stack is empty")
        else:
            popped = self.top.data
            self.top = self.top.next
            self.count -= 1
            print(popped, "popped from stack")

    # Peek operation
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Top element:", self.top.data)

    # Check if stack is empty
    def is_empty(self):
        return self.top is None

    # Return size of stack
    def size(self):
        return self.count

    # Display stack
    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack elements (Top to Bottom):")
            temp = self.top

            while temp:
                print(temp.data)
                temp = temp.next


# Driver Program
s = Stack()

while True:

    print("\nName: Almash Lakdawala")
    print("Enrollment: 26PG030052")

    print("\n--- Stack Menu ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Check if Empty")
    print("5. Size")
    print("6. Display")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = int(input("Enter element to push: "))
        s.push(item)

    elif choice == 2:
        s.pop()

    elif choice == 3:
        s.peek()

    elif choice == 4:
        if s.is_empty():
            print("Stack is Empty")
        else:
            print("Stack is Not Empty")

    elif choice == 5:
        print("Stack Size:", s.size())

    elif choice == 6:
        s.display()

    elif choice == 7:
        print("Exiting...")
        break

    else:
        print("Invalid Choice! Please try again.")