# Practical 5(a): Binary Search Tree (BST) Insertion
# Binary Search Tree (BST) follows the following rules:
# 1. Left child contains smaller value than the parent node.
# 2. Right child contains greater value than the parent node.
# 3. Duplicate values are not allowed.


# Node class
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# BST class
class BinarySearchTree:

    def __init__(self):
        self.root = None

    # Insert a new node
    def insert(self, data):

        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_node(self.root, data)

    # Recursive insertion
    def insert_node(self, current, data):

        if data < current.data:

            if current.left is None:
                current.left = Node(data)
            else:
                self.insert_node(current.left, data)

        elif data > current.data:

            if current.right is None:
                current.right = Node(data)
            else:
                self.insert_node(current.right, data)

        else:
            print("Duplicate values are not allowed.")

    # Search an element
    def search(self, data):

        if self.search_node(self.root, data):
            print(data, "found in BST.")
        else:
            print(data, "not found in BST.")

    # Recursive search
    def search_node(self, current, data):

        if current is None:
            return False

        if current.data == data:
            return True

        elif data < current.data:
            return self.search_node(current.left, data)

        else:
            return self.search_node(current.right, data)

    # Delete a node
    def delete(self, data):

        self.root = self.delete_node(self.root, data)

    # Recursive deletion
    def delete_node(self, current, data):

        if current is None:
            return current

        if data < current.data:
            current.left = self.delete_node(current.left, data)

        elif data > current.data:
            current.right = self.delete_node(current.right, data)

        else:

            # Node with no left child
            if current.left is None:
                return current.right

            # Node with no right child
            elif current.right is None:
                return current.left

            # Node with two children
            temp = self.find_min(current.right)
            current.data = temp.data
            current.right = self.delete_node(current.right, temp.data)

        return current

    # Find minimum node
    def find_min(self, current):

        while current.left is not None:
            current = current.left

        return current

    # Inorder Traversal
    def inorder(self):

        self.inorder_traversal(self.root)
        print()

    # Recursive inorder traversal
    def inorder_traversal(self, node):

        if node is not None:

            self.inorder_traversal(node.left)
            print(node.data, end=" ")
            self.inorder_traversal(node.right)


# ---------------- Driver Code ----------------

bst = BinarySearchTree()

n = int(input("Enter number of nodes: "))

for i in range(n):
    value = int(input("Enter value: "))
    bst.insert(value)

print("\nInorder Traversal:")
bst.inorder()

# Search
value = int(input("\nEnter value to search: "))
bst.search(value)

# Delete
value = int(input("\nEnter value to delete: "))
bst.delete(value)

print("\nBST after deletion:")
bst.inorder()