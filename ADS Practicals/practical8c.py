
import heapq
from collections import Counter


def huffman_encoding(text):
    if not text:
        return {}

    frequency = Counter(text)
    heap = []
    counter = 0

    for char, freq in frequency.items():
        heapq.heappush(heap, (freq, counter, char))
        counter += 1

    while len(heap) > 1:
        f1, _, left = heapq.heappop(heap)
        f2, _, right = heapq.heappop(heap)

        merged = (left, right)

        heapq.heappush(
            heap,
            (f1 + f2, counter, merged)
        )
        counter += 1

    root = heap[0][2]
    codes = {}

    def generate_codes(node, code):
        if isinstance(node, str):
            codes[node] = code or "0"
            return

        generate_codes(node[0], code + "0")
        generate_codes(node[1], code + "1")

    generate_codes(root, "")
    return codes


# Student Details
print("Name: Almash Lakdawala")
print("Enrollment No.: 26PG030052")

# Input text
text = "HUFFMAN ENCODING"

codes = huffman_encoding(text)

print("Huffman Codes:")

for char, code in codes.items():
    print(repr(char), ":", code)

encoded = "".join(codes[ch] for ch in text)
print("Encoded String:", encoded)
