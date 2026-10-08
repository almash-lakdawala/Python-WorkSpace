# PRACTICAL 5(d): FIBONACCI HEAP IMPLEMENTATION

class FibonacciNode:

    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.parent = None
        self.child = None
        self.left = self
        self.right = self


class FibonacciHeap:

    def __init__(self):
        self.min = None
        self.n = 0

    # INSERT
    def insert(self, key):

        node = FibonacciNode(key)

        if self.min is None:
            self.min = node

        else:
            node.right = self.min.right
            node.left = self.min

            self.min.right.left = node
            self.min.right = node

            if node.key < self.min.key:
                self.min = node

        self.n += 1

    # GET MINIMUM
    def get_min(self):

        if self.min is None:
            return None

        return self.min.key

    # SEARCH
    def search(self, key):

        if self.min is None:
            return False

        return self._search(self.min, key, set())

    def _search(self, node, key, visited):

        current = node

        while current not in visited:

            visited.add(current)

            if current.key == key:
                return True

            if current.child:

                if self._search(current.child, key, visited):
                    return True

            current = current.right

        return False

    # EXTRACT MINIMUM
    def extract_min(self):

        if self.min is None:
            print("Fibonacci Heap is empty")
            return None

        minimum = self.min

        # Add children to root list
        if minimum.child:

            children = []
            child = minimum.child

            while True:

                children.append(child)
                child = child.right

                if child == minimum.child:
                    break

            for child in children:

                child.parent = None

                child.left.right = child.right
                child.right.left = child.left

                child.left = self.min
                child.right = self.min.right

                self.min.right.left = child
                self.min.right = child

        # Remove minimum
        minimum.left.right = minimum.right
        minimum.right.left = minimum.left

        if minimum == minimum.right:

            self.min = None

        else:

            self.min = minimum.right
            self._find_min()

        self.n -= 1

        return minimum.key

    # FIND NEW MINIMUM
    def _find_min(self):

        current = self.min
        minimum = current

        while True:

            if current.key < minimum.key:
                minimum = current

            current = current.right

            if current == self.min:
                break

        self.min = minimum

    # DISPLAY
    def display(self):

        if self.min is None:
            print("Fibonacci Heap is empty")
            return

        print("Fibonacci Heap Root List:")

        current = self.min

        while True:

            print(current.key, end=" ")

            current = current.right

            if current == self.min:
                break

        print()


# PROGRAM

h = FibonacciHeap()

print("Name: Almash Lakdawala")
print("Enrollment: 26PG030052")

for value in [20, 10, 30, 5, 40, 15]:
    h.insert(value)

h.display()

print("Minimum:", h.get_min())

print(
    "Search 30:",
    "Found" if h.search(30) else "Not Found"
)

print("Extracted Minimum:", h.extract_min())

h.display()