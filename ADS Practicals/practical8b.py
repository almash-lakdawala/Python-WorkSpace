
import heapq


def prim(graph, start=0):
    if start not in graph:
        raise ValueError("Starting vertex not found")

    visited = set()
    min_heap = [(0, start, -1)]
    mst = []
    total_cost = 0

    while min_heap:
        weight, vertex, parent = heapq.heappop(min_heap)

        if vertex in visited:
            continue

        visited.add(vertex)
        total_cost += weight

        if parent != -1:
            mst.append((parent, vertex, weight))

        for neighbour, edge_weight in graph[vertex]:
            if neighbour not in visited:
                heapq.heappush(
                    min_heap,
                    (edge_weight, neighbour, vertex)
                )

    if len(visited) != len(graph):
        raise ValueError("Graph is disconnected")

    return mst, total_cost


# Student Details
print("Name: Almash Lakdawala")
print("Enrollment No.: 26PG030052")

# Weighted undirected graph
graph = {
    0: [(1, 10), (2, 6), (3, 5)],
    1: [(0, 10), (3, 15)],
    2: [(0, 6), (3, 4)],
    3: [(0, 5), (1, 15), (2, 4)]
}

mst, cost = prim(graph)

print("Prim MST:", mst)
print("Total Cost:", cost)
