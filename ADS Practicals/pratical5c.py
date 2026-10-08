# PRACTICAL 5(c): BINOMIAL HEAP IMPLEMENTATION

class BinomialNode:

    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.parent = None
        self.child = None
        self.sibling = None


class BinomialHeap:

    def __init__(self):
        self.head = None

    # Link two binomial trees
    def link(self, y, z):

        y.parent = z
        y.sibling = z.child
        z.child = y
        z.degree += 1

    # Merge root lists
    def merge_root_lists(self, other):

        new_head = None
        tail = None

        h1 = self.head
        h2 = other.head

        while h1 and h2:

            if h1.degree <= h2.degree:
                node = h1
                h1 = h1.sibling
            else:
                node = h2
                h2 = h2.sibling

            if new_head is None:
                new_head = node
                tail = node
            else:
                tail.sibling = node
                tail = node

        remaining = h1 if h1 else h2

        if tail:
            tail.sibling = remaining
        else:
            new_head = remaining

        return new_head

    # Union of two binomial heaps
    def union(self, other):

        result = BinomialHeap()

        result.head = self.merge_root_lists(other)

        if result.head is None:
            return result

        prev = None
        curr = result.head
        next_node = curr.sibling

        while next_node:

            if (
                curr.degree != next_node.degree
                or (
                    next_node.sibling
                    and next_node.sibling.degree == curr.degree
                )
            ):

                prev = curr
                curr = next_node

            elif curr.key <= next_node.key:

                curr.sibling = next_node.sibling

                result.link(next_node, curr)

            else:

                if prev is None:
                    result.head = next_node
                else:
                    prev.sibling = next_node

                result.link(curr, next_node)

                curr = next_node

            next_node = curr.sibling

        return result

    # Insert a key
    def insert(self, key):

        new_heap = BinomialHeap()

        new_heap.head = BinomialNode(key)

        merged = self.union(new_heap)

        self.head = merged.head

    # Get minimum value
    def get_min(self):

        if self.head is None:
            return None

        minimum = self.head
        current = self.head.sibling

        while current:

            if current.key < minimum.key:
                minimum = current

            current = current.sibling

        return minimum.key

    # Display tree
    def display_tree(self, node, level=0):

        if node is None:
            return

        print("    " * level + str(node.key))

        child = node.child

        while child:

            self.display_tree(child, level + 1)

            child = child.sibling

    # Display complete heap
    def display(self):

        if self.head is None:
            print("Binomial Heap is empty")
            return

        print("Binomial Heap:")

        current = self.head

        while current:

            print(f"B{current.degree} Tree:")

            self.display_tree(current)

            current = current.sibling


# PROGRAM

h = BinomialHeap()

print("Name: Almash Lakdawala")
print("Enrollment: 26PG030052")

for value in [20, 10, 30, 5, 40, 15]:
    h.insert(value)

h.display()

print("Minimum:", h.get_min())