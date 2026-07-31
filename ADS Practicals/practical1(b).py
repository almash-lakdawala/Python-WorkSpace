"""
Practical 1(b): Stack Implementation using Linked List

Objective:
To implement the Stack data structure using a Linked List
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

In a Linked List implementation, each element is stored in a node.
Each node contains:
1. Data
2. Address of the next node

The 'top' pointer always points to the first node of the linked list.
Insertion and deletion are performed at the beginning of the list,
making both operations O(1).
"""


# Node class represents each element of the linked list
class Node:

    # Constructor to initialize node with data
    def __init__(self, data):
        self.data = data          # Store the data
        self.next = None          # Pointer to the next node


# Stack class using Linked List
class Stack:

    # Constructor to initialize an empty stack
    def __init__(self):
        self.top = None           # Top pointer
        self.count = 0            # Counter to keep track of stack size

    # Push operation: Insert a new node at the beginning
    def push(self, item):

        # Create a new node
        new_node = Node(item)

        # New node points to current top
        new_node.next = self.top

        # Update top pointer
        self.top = new_node

        # Increase stack size
        self.count += 1

    # Pop operation: Remove and return the top node
    def pop(self):

        # Check if stack is empty
        if self.is_empty():
            print("Stack Underflow")
            return None

        # Store the top node temporarily
        temp = self.top

        # Move top pointer to next node
        self.top = self.top.next

        # Decrease stack size
        self.count -= 1

        # Return deleted data
        return temp.data

    # Peek operation: Return the top element without removing it
    def peek(self):

        if self.is_empty():
            return None

        return self.top.data

    # Check whether the stack is empty
    def is_empty(self):

        return self.top is None

    # Return the total number of elements
    def size(self):

        return self.count

    # Display stack elements from top to bottom
    def display(self):

        if self.is_empty():
            print("Stack is Empty")
            return

        print("Stack (Top to Bottom):")

        temp = self.top

        # Traverse the linked list
        while temp:
            print(temp.data)
            temp = temp.next


# ---------------- Driver Code ----------------

# Create a Stack object
stack = Stack()

# Push elements into the stack
stack.push(10)
stack.push(20)
stack.push(30)

# Display stack
stack.display()

# Display top element
print("Top:", stack.peek())

# Display stack size
print("Size:", stack.size())

# Remove top element
print("Removed:", stack.pop())

# Display updated stack
stack.display()

# Check whether stack is empty
print("Is Empty:", stack.is_empty())