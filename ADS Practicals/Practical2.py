class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None

    # Insert
    def insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)

        elif data > root.data:
            root.right = self.insert(root.right, data)

        return root

    # Search
    def search(self, root, key):
        if root is None:
            return False

        if root.data == key:
            return True

        if key < root.data:
            return self.search(root.left, key)

        return self.search(root.right, key)

    # Find minimum
    def minimum(self, root):
        current = root

        while current.left is not None:
            current = current.left

        return current

    # Delete
    def delete(self, root, key):

        if root is None:
            return root

        if key < root.data:
            root.left = self.delete(root.left, key)

        elif key > root.data:
            root.right = self.delete(root.right, key)

        else:

            # No child
            if root.left is None and root.right is None:
                return None

            # Only right child
            if root.left is None:
                return root.right

            # Only left child
            if root.right is None:
                return root.left

            # Two children
            temp = self.minimum(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)

        return root

    # Inorder
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")

    # Preorder
    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    # Postorder
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")


# PROGRAM

print("Name: Almash Lakdawala")
print("Enrollment: 26PG030052")

bst = BST()

values = [50, 30, 70, 20, 40, 60, 80]

# Insert values
for value in values:
    bst.root = bst.insert(bst.root, value)


# Inorder Traversal
print("\nInorder Traversal:")
bst.inorder(bst.root)


# Preorder Traversal
print("\nPreorder Traversal:")
bst.preorder(bst.root)


# Postorder Traversal
print("\nPostorder Traversal:")
bst.postorder(bst.root)


# Search
key = 40

print("\n\nSearching for:", key)

if bst.search(bst.root, key):
    print("Element found")
else:
    print("Element not found")


# Delete
delete_value = 30

print("\nBefore deletion:")
bst.inorder(bst.root)

bst.root = bst.delete(bst.root, delete_value)

print("\nAfter deleting", delete_value, ":")
bst.inorder(bst.root)