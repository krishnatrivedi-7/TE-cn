# Distance Vector Routing (Bellman-Ford Algorithm)

def distance_vector_routing(graph, start):
    distance = {node: float('inf') for node in graph}
    distance[start] = 0

    # Relax edges |V|-1 times
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, cost in graph[u].items():
                if distance[u] + cost < distance[v]:
                    distance[v] = distance[u] + cost

    return distance


# Example network graph (undirected)
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 5, 'D': 10},
    'C': {'A': 2, 'B': 5, 'D': 3},
    'D': {'B': 10, 'C': 3}
}

start = 'A'
result = distance_vector_routing(graph, start)
print(f"Shortest distances from {start}:")
for node, dist in result.items():
    print(f"{start} → {node} = {dist}")

# Link State Routing (Dijkstra’s Algorithm)

def link_state_routing(graph, start):
    visited = set()
    distance = {node: float('inf') for node in graph}
    distance[start] = 0

    while len(visited) < len(graph):
        # pick the unvisited node with the smallest distance
        min_node = min((node for node in graph if node not in visited),
                       key=lambda x: distance[x])

        visited.add(min_node)
        for neighbor, cost in graph[min_node].items():
            if distance[min_node] + cost < distance[neighbor]:
                distance[neighbor] = distance[min_node] + cost

    return distance


# Example network
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 5, 'D': 10},
    'C': {'A': 2, 'B': 5, 'D': 3},
    'D': {'B': 10, 'C': 3}
}

start = 'A'
result = link_state_routing(graph, start)
print(f"\nShortest distances from {start}:")
for node, dist in result.items():
    print(f"{start} → {node} = {dist}")
