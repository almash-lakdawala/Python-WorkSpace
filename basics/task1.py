
import heapq


class WeightedGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def dijkstra(self, source):
        if source not in self.graph:
            print("Source vertex not found")
            return {}

        distance = {
            vertex: float("inf")
            for vertex in self.graph
        }

        distance[source] = 0
        priority_queue = [(0, source)]

        while priority_queue:
            current_distance, current_vertex = (
                heapq.heappop(priority_queue)
            )

            if current_distance > distance[current_vertex]:
                continue

            for neighbour, weight in self.graph[current_vertex]:
                new_distance = current_distance + weight

                if new_distance < distance[neighbour]:
                    distance[neighbour] = new_distance

                    heapq.heappush(
                        priority_queue,
                        (new_distance, neighbour)
                    )

        return distance


# Student Details
print("Name: Almash Lakdawala")
print("Enrollment No.: 26PG030052")

# Create weighted graph
g = WeightedGraph()

edges = [
    (0, 1, 4),
    (0, 2, 2),
    (1, 2, 1),
    (1, 3, 5),
    (2, 3, 8),
    (2, 4, 10),
    (3, 4, 2)
]

for u, v, weight in edges:
    g.add_edge(u, v, weight)

# Find shortest distances
source = 0
shortest_distances = g.dijkstra(source)

print("\nShortest distances from vertex", source)

for vertex, distance in sorted(shortest_distances.items()):
    print("Vertex", vertex, ":", distance)
