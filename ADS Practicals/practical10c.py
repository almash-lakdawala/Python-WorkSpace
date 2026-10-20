
def hamiltonian_cycle(graph):
    n = len(graph)
    path = [-1] * n
    path[0] = 0

    def is_safe(vertex, pos):
        if graph[path[pos - 1]][vertex] == 0:
            return False

        if vertex in path:
            return False

        return True

    def solve(pos):
        if pos == n:
            return graph[path[pos - 1]][path[0]] != 0

        for vertex in range(1, n):
            if is_safe(vertex, pos):
                path[pos] = vertex

                if solve(pos + 1):
                    return True

                path[pos] = -1

        return False

    if solve(1):
        return path + [path[0]]

    return None


# Student Details
print("Name: Almash Lakdawala")
print("Enrollment No.: 26PG030052")

# Adjacency matrix of the graph
graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
]

cycle = hamiltonian_cycle(graph)

if cycle:
    print("Hamiltonian Cycle:", " -> ".join(map(str, cycle)))
else:
    print("No Hamiltonian Cycle Exists")
