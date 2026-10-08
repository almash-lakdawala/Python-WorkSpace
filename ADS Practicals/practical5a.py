# PRACTICAL 5(a): MIN HEAP IMPLEMENTATION

class MinHeap:

    def __init__(self):
        self.heap = []

    # Insert operation
    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    # Heapify Up
    def _heapify_up(self, index):

        while index > 0:

            parent = (index - 1) // 2

            if self.heap[index] < self.heap[parent]:

                self.heap[index], self.heap[parent] = (
                    self.heap[parent],
                    self.heap[index]
                )

                index = parent

            else:
                break

    # Delete minimum
    def delete_min(self):

        if not self.heap:
            print("Heap is empty")
            return None

        minimum = self.heap[0]

        last = self.heap.pop()

        if self.heap:

            self.heap[0] = last
            self._heapify_down(0)

        return minimum

    # Heapify Down
    def _heapify_down(self, index):

        n = len(self.heap)

        while True:

            smallest = index

            left = 2 * index + 1
            right = 2 * index + 2

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != index:

                self.heap[index], self.heap[smallest] = (
                    self.heap[smallest],
                    self.heap[index]
                )

                index = smallest

            else:
                break

    # Search operation
    def search(self, value):
        return value in self.heap

    # Display heap
    def display(self):
        print("Min Heap:", self.heap)


# PROGRAM

h = MinHeap()

for value in [20, 10, 30, 5, 40, 15]:
    h.insert(value)

h.display()

print(
    "Search 30:",
    "Found" if h.search(30) else "Not Found"
)

print("Deleted Minimum:", h.delete_min())

h.display()