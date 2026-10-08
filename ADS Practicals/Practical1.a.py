class Stack:

    def __init__(self, capacity):
        self.stack = []
        self.capacity = capacity

    # Push Operation
    def push(self, item):
        if self.isFull():
            print("Stack is full. Cannot push item.")
        else:
            self.stack.append(item)
            print(f"Pushed {item} to stack.")

    # Pop Operation
    def pop(self):
        if self.isEmpty():
            print("Stack is empty. Cannot pop item.")
            return None
        else:
            item = self.stack.pop()
            print(f"Popped {item} from stack.")
            return item

    # Peek Operation
    def peek(self):
        if self.isEmpty():
            print("Stack is empty. Cannot peek.")
            return None
        else:
            item = self.stack[-1]
            print(f"Top item is {item}.")
            return item

    # Check if stack is empty
    def isEmpty(self):
        return len(self.stack) == 0

    # Check if stack is full
    def isFull(self):
        return len(self.stack) == self.capacity

    # Get the size of the stack
    def size(self):
        return len(self.stack)

    # Display the stack
    def display(self):
        if self.isEmpty():
            print("Stack is empty.")
        else:
            print("Stack contents:", self.stack)


# Main Program
capacity = int(input("Enter the capacity of the stack: "))
stack = Stack(capacity)

while True:

    print("\nName: YNVS BHASKARA SASTRY")
    print("Enrollment: 26PG030109")

    print("\nStack Operations:")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Check if stack is empty")
    print("5. Check if stack is full")
    print("6. Get size of stack")
    print("7. Display stack contents")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        item = input("Enter item to push: ")
        stack.push(item)

    elif choice == '2':
        stack.pop()

    elif choice == '3':
        stack.peek()

    elif choice == '4':
        if stack.isEmpty():
            print("Stack is empty.")
        else:
            print("Stack is not empty.")

    elif choice == '5':
        if stack.isFull():
            print("Stack is full.")
        else:
            print("Stack is not full.")

    elif choice == '6':
        print(f"Size of stack: {stack.size()}")

    elif choice == '7':
        stack.display()

    elif choice == '8':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")