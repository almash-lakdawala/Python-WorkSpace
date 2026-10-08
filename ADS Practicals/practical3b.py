RED = "RED"
BLACK = "BLACK"


class Node:

    def __init__(self, key):
        self.key = key
        self.color = RED
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:

    def __init__(self):
        self.root = None
        self.rotation_count = 0

    # Left Rotation
    def left_rotate(self, x):

        y = x.right
        x.right = y.left

        if y.left is not None:
            y.left.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

        self.rotation_count += 1

    # Right Rotation
    def right_rotate(self, y):

        x = y.left
        y.left = x.right

        if x.right is not None:
            x.right.parent = y

        x.parent = y.parent

        if y.parent is None:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x

        x.right = y
        y.parent = x

        self.rotation_count += 1

    # Standard BST insertion
    def bst_insert(self, key):

        new_node = Node(key)
        parent = None
        current = self.root

        while current is not None:

            parent = current

            if key < current.key:
                current = current.left

            elif key > current.key:
                current = current.right

            else:
                print("Duplicate key ignored:", key)
                return None

        new_node.parent = parent

        if parent is None:
            self.root = new_node

        elif key < parent.key:
            parent.left = new_node

        else:
            parent.right = new_node

        return new_node

    # Fix Red-Black violations
    def insert_fixup(self, z):

        while z != self.root and z.parent.color == RED:

            parent = z.parent
            grandparent = parent.parent

            # Parent is left child
            if parent == grandparent.left:

                uncle = grandparent.right

                # Case 1: Uncle is RED
                if uncle is not None and uncle.color == RED:

                    parent.color = BLACK
                    uncle.color = BLACK
                    grandparent.color = RED

                    print("Recoloring at", grandparent.key)

                    z = grandparent

                else:

                    # Case 2: LR Case
                    if z == parent.right:

                        print("LR Rotation at", grandparent.key)

                        z = parent
                        self.left_rotate(z)

                        parent = z.parent
                        grandparent = parent.parent

                    # Case 3: LL Case
                    parent.color = BLACK
                    grandparent.color = RED

                    print("LL Rotation at", grandparent.key)

                    self.right_rotate(grandparent)

            # Parent is right child
            else:

                uncle = grandparent.left

                # Case 1: Uncle is RED
                if uncle is not None and uncle.color == RED:

                    parent.color = BLACK
                    uncle.color = BLACK
                    grandparent.color = RED

                    print("Recoloring at", grandparent.key)

                    z = grandparent

                else:

                    # Case 2: RL Case
                    if z == parent.left:

                        print("RL Rotation at", grandparent.key)

                        z = parent
                        self.right_rotate(z)

                        parent = z.parent
                        grandparent = parent.parent

                    # Case 3: RR Case
                    parent.color = BLACK
                    grandparent.color = RED

                    print("RR Rotation at", grandparent.key)

                    self.left_rotate(grandparent)

        # Root must always be BLACK
        self.root.color = BLACK

    # Insert into Red-Black Tree
    def insert(self, key):

        new_node = self.bst_insert(key)

        if new_node is None:
            return

        # New root must be BLACK
        if new_node == self.root:
            new_node.color = BLACK
            return

        # Fix violations
        self.insert_fixup(new_node)

    # Inorder traversal
    def inorder(self, node):

        if node is not None:

            self.inorder(node.left)

            print(
                f"{node.key}({node.color[0]})",
                end=" "
            )

            self.inorder(node.right)

    # Preorder traversal
    def preorder(self, node):

        if node is not None:

            print(
                f"{node.key}({node.color[0]})",
                end=" "
            )

            self.preorder(node.left)
            self.preorder(node.right)

    # Calculate height
    def height(self, node):

        if node is None:
            return 0

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1 + max(left_height, right_height)


# PROGRAM

print("Name: Almash Lakdawala")
print("Enrollment: 26PG030052")

tree = RedBlackTree()

n = int(input("Enter number of elements: "))

print("Enter elements:")

for i in range(n):
    key = int(input())
    tree.insert(key)

print("\nInorder Traversal:")
tree.inorder(tree.root)

print("\n\nPreorder Traversal:")
tree.preorder(tree.root)

print("\n\nTree Height:", tree.height(tree.root))

print("Total Rotations:", tree.rotation_count)