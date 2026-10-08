# B-TREE IMPLEMENTATION

class BTreeNode:

    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []


class BTree:

    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t

    # SEARCH
    def search(self, node, key):

        i = 0

        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        if i < len(node.keys) and key == node.keys[i]:
            return node

        if node.leaf:
            return None

        return self.search(node.children[i], key)

    # SPLIT CHILD
    def split_child(self, parent, i):

        t = self.t
        old_child = parent.children[i]

        new_child = BTreeNode(old_child.leaf)

        # Middle key
        middle_key = old_child.keys[t - 1]

        # Keys for new child
        new_child.keys = old_child.keys[t:]

        # Keep first half in old child
        old_child.keys = old_child.keys[:t - 1]

        # If internal node, split children
        if not old_child.leaf:
            new_child.children = old_child.children[t:]
            old_child.children = old_child.children[:t]

        # Add new child
        parent.children.insert(i + 1, new_child)

        # Move middle key to parent
        parent.keys.insert(i, middle_key)

    # INSERT
    def insert(self, key):

        root = self.root

        # Root is full
        if len(root.keys) == 2 * self.t - 1:

            new_root = BTreeNode(False)
            self.root = new_root

            new_root.children.append(root)

            self.split_child(new_root, 0)

            self.insert_non_full(new_root, key)

        else:
            self.insert_non_full(root, key)

    # INSERT INTO NON-FULL NODE
    def insert_non_full(self, node, key):

        i = len(node.keys) - 1

        # Leaf node
        if node.leaf:

            node.keys.append(0)

            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1

            node.keys[i + 1] = key

        else:

            while i >= 0 and key < node.keys[i]:
                i -= 1

            i += 1

            # Child is full
            if len(node.children[i].keys) == 2 * self.t - 1:

                self.split_child(node, i)

                if key > node.keys[i]:
                    i += 1

            self.insert_non_full(node.children[i], key)

    # INORDER TRAVERSAL
    def inorder(self, node=None):

        if node is None:
            node = self.root

        for i in range(len(node.keys)):

            if not node.leaf:
                self.inorder(node.children[i])

            print(node.keys[i], end=" ")

        if not node.leaf:
            self.inorder(node.children[len(node.keys)])

    # DISPLAY TREE STRUCTURE
    def display_tree(self, node=None, level=0):

        if node is None:
            node = self.root

        print("    " * level + str(node.keys))

        if not node.leaf:

            for child in node.children:
                self.display_tree(child, level + 1)


# PROGRAM

print("=" * 50)
print("                  B-TREE")
print("=" * 50)

# Minimum degree
btree = BTree(2)

print("Name: Almash Lakdawala")
print("Enrollment: 26PG030052")

# Values to insert
values = [10, 20, 5, 6, 12, 30, 7, 17]

print("\nValues inserted:")
print(values)

# Insert values
for value in values:
    btree.insert(value)

# TREE STRUCTURE
print("\nB-Tree Structure:")
btree.display_tree()

# TRAVERSAL
print("\nB-Tree Inorder Traversal:")
btree.inorder()

# SEARCH
key = 12

print("\n\nSearching for:", key)

if btree.search(btree.root, key):
    print(key, "found in B-Tree")
else:
    print(key, "not found in B-Tree")