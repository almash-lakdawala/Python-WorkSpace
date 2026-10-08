class ThreadedNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

        # True  -> right pointer is a thread
        # False -> right pointer is a child
        self.rightThread = False


class ThreadedBST:

    def __init__(self):
        self.root = None

    # -------------------------
    # INSERTION
    # -------------------------
    def insert(self, data):

        new_node = ThreadedNode(data)

        if self.root is None:
            self.root = new_node
            return

        current = self.root

        while True:

            if data < current.data:

                if current.left is None:

                    new_node.right = current
                    new_node.rightThread = True

                    current.left = new_node
                    return

                else:
                    current = current.left

            elif data > current.data:

                if current.right is None or current.rightThread:

                    new_node.right = current.right
                    new_node.rightThread = current.rightThread

                    current.right = new_node
                    current.rightThread = False

                    return

                else:
                    current = current.right

            else:
                print("Duplicate value not allowed")
                return

    # -------------------------
    # FIND LEFTMOST NODE
    # -------------------------
    def leftmost(self, node):

        if node is None:
            return None

        while node.left is not None:
            node = node.left

        return node

    # -------------------------
    # THREADED INORDER
    # -------------------------
    def inorder(self):

        current = self.leftmost(self.root)

        while current is not None:

            print(current.data, end=" ")

            if current.rightThread:
                current = current.right
            else:
                current = self.leftmost(current.right)


# -------------------------
# PROGRAM
# -------------------------

print("Name: Almash Lakdawala")
print("Enrollment: 26PG030052")

tree = ThreadedBST()

values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    tree.insert(value)

print("\nRight Threaded BST Inorder Traversal:")
tree.inorder()

print()