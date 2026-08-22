# Practical 6: Single Threaded Binary Search Tree

# Node class
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.thread = False


# Single Threaded BST class
class SingleThreadedBST:

    def __init__(self):
        self.root = None

    # Insert a node
    def insert(self, data):

        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return

        current = self.root
        parent = None

        while current:

            parent = current

            if data < current.data:

                if current.left is None:
                    break

                current = current.left

            elif data > current.data:

                if current.thread or current.right is None:
                    break

                current = current.right

            else:
                print("Duplicate value not allowed.")
                return

        if data < parent.data:

            parent.left = new_node
            new_node.right = parent
            new_node.thread = True

        else:

            new_node.right = parent.right
            new_node.thread = True

            parent.right = new_node
            parent.thread = False

    # Leftmost node
    def leftmost(self, node):

        while node and node.left:
            node = node.left

        return node

    # Inorder Traversal
    def inorder(self):

        current = self.leftmost(self.root)

        while current:

            print(current.data, end=" ")

            if current.thread:
                current = current.right
            else:
                current = self.leftmost(current.right)

        print()


# Driver Code
tree = SingleThreadedBST()

n = int(input("Enter number of nodes: "))

for i in range(n):
    value = int(input("Enter value: "))
    tree.insert(value)

print("\nInorder Traversal:")
tree.inorder()