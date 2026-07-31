# Practical 1(a): Stack Implementation using Array (Python List)
"""
Practical 1(a): Stack Implementation using Array

Objective:
To implement the Stack data structure using a Python list (Array)
and perform the following operations:
1. Push
2. Pop
3. Peek
4. is_empty
5. Size
6. Display

Theory:
A Stack is a linear data structure that follows the LIFO
(Last In First Out) principle.
"""
# The last element inserted into the stack is the first one to be removed.

class Stack:

    # Constructor to initialize an empty stack
    def __init__(self):
        self.items = []      # Python list is used as an array to store stack elements

    # Push operation: Insert an element at the top of the stack
    def push(self, item):
        self.items.append(item)

    # Pop operation: Remove and return the top element of the stack
    def pop(self):
        # Check if the stack is empty
        if self.is_empty():
            print("Stack Underflow")
            return None

        # Remove and return the last element
        return self.items.pop()

    # Peek operation: Return the top element without removing it
    def peek(self):
        if self.is_empty():
            return None

        return self.items[-1]

    # Check whether the stack is empty
    def is_empty(self):
        return len(self.items) == 0

    # Return the total number of elements in the stack
    def size(self):
        return len(self.items)

    # Display all stack elements from top to bottom
    def display(self):
        if self.is_empty():
            print("Stack is Empty")
        else:
            print("Stack (Top to Bottom):")

            # Print elements in reverse order because
            # the last inserted element is the top of the stack
            for item in reversed(self.items):
                print(item)


# ---------------- Driver Code ----------------

# Create an object of Stack class
stack = Stack()

# Push elements into the stack
stack.push(10)
stack.push(20)
stack.push(30)

# Display all stack elements
stack.display()

# Display the top element
print("Top:", stack.peek())

# Display the total number of elements
print("Size:", stack.size())

# Remove the top element
print("Removed:", stack.pop())

# Display stack after pop operation
stack.display()

# Check whether the stack is empty
print("Is Empty:", stack.is_empty())