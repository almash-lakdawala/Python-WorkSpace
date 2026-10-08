class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:

    def __init__(self):
        self.rotation_count = 0

    # Get height
    def height(self, node):
        if node is None:
            return 0
        return node.height

    # Get maximum
    def max_value(self, a, b):
        return a if a > b else b

    # Get balance factor
    def get_balance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    # Right Rotation - LL Case
    def right_rotate(self, y):

        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + self.max_value(
            self.height(y.left),
            self.height(y.right)
        )

        x.height = 1 + self.max_value(
            self.height(x.left),
            self.height(x.right)
        )

        self.rotation_count += 1

        return x

    # Left Rotation - RR Case
    def left_rotate(self, x):

        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + self.max_value(
            self.height(x.left),
            self.height(x.right)
        )

        y.height = 1 + self.max_value(
            self.height(y.left),
            self.height(y.right)
        )

        self.rotation_count += 1

        return y

    # Insert node
    def insert(self, node, key):

        # Standard BST insertion
        if node is None:
            return Node(key)

        if key < node.key:
            node.left = self.insert(node.left, key)

        elif key > node.key:
            node.right = self.insert(node.right, key)

        else:
            print("Duplicate key ignored:", key)
            return node

        # Update height
        node.height = 1 + self.max_value(
            self.height(node.left),
            self.height(node.right)
        )

        # Calculate balance factor
        balance = self.get_balance(node)

        # LL Case
        if balance > 1 and key < node.left.key:
            print("LL Rotation at", node.key)
            return self.right_rotate(node)

        # RR Case
        if balance < -1 and key > node.right.key:
            print("RR Rotation at", node.key)
            return self.left_rotate(node)

        # LR Case
        if balance > 1 and key > node.left.key:
            print("LR Rotation at", node.key)
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # RL Case
        if balance < -1 and key < node.right.key:
            print("RL Rotation at", node.key)
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    # Inorder traversal
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.key, end=" ")
            self.inorder(node.right)

    # Preorder traversal
    def preorder(self, node):
        if node:
            print(node.key, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)


# PROGRAM

print("Name: Almash Lakdawala")
print("Enrollment: 26PG030052")

tree = AVLTree()
root = None

n = int(input("Enter number of elements: "))

print("Enter elements:")

for i in range(n):
    key = int(input())
    root = tree.insert(root, key)

print("\nInorder Traversal:")
tree.inorder(root)

print("\n\nPreorder Traversal:")
tree.preorder(root)

print("\n\nTree Height:", tree.height(root))
print("Total Rotations:", tree.rotation_count)