
def kruskal(vertices, edges):
    parent = list(range(vertices))
    rank = [0] * vertices

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)

        if root_x == root_y:
            return False

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

        return True

    edges.sort(key=lambda edge: edge[2])
    mst = []
    total_cost = 0

    for u, v, weight in edges:
        if union(u, v):
            mst.append((u, v, weight))
            total_cost += weight

        if len(mst) == vertices - 1:
            break

    if len(mst) != vertices - 1:
        raise ValueError("Graph is disconnected")

    return mst, total_cost


# Student Details
print("Name: Almash Lakdawala")
print("Enrollment No.: 26PG030052")

# Graph edges: (vertex1, vertex2, weight)
vertices = 4
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

mst, cost = kruskal(vertices, edges)

print("Kruskal MST:", mst)
print("Total Cost:", cost)
