# PRACTICAL 5(b): MAX HEAP IMPLEMENTATION

class MaxHeap:

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

            if self.heap[index] > self.heap[parent]:

                self.heap[index], self.heap[parent] = (
                    self.heap[parent],
                    self.heap[index]
                )

                index = parent

            else:
                break

    # Delete maximum
    def delete_max(self):

        if not self.heap:
            print("Heap is empty")
            return None

        maximum = self.heap[0]

        last = self.heap.pop()

        if self.heap:

            self.heap[0] = last
            self._heapify_down(0)

        return maximum

    # Heapify Down
    def _heapify_down(self, index):

        n = len(self.heap)

        while True:

            largest = index

            left = 2 * index + 1
            right = 2 * index + 2

            if left < n and self.heap[left] > self.heap[largest]:
                largest = left

            if right < n and self.heap[right] > self.heap[largest]:
                largest = right

            if largest != index:

                self.heap[index], self.heap[largest] = (
                    self.heap[largest],
                    self.heap[index]
                )

                index = largest

            else:
                break

    # Search operation
    def search(self, value):
        return value in self.heap

    # Display heap
    def display(self):
        print("Max Heap:", self.heap)


# PROGRAM

h = MaxHeap()

print("Name: Almash Lakdawala")
print("Enrollment: 26PG030052")

for value in [20, 10, 30, 5, 40, 15]:
    h.insert(value)

h.display()

print(
    "Search 20:",
    "Found" if h.search(20) else "Not Found"
)

print("Deleted Maximum:", h.delete_max())

h.display()