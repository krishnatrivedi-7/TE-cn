def get_graph():
    g = {}
    n = int(input("Enter no. of nodes: "))
    for _ in range(n):
        node = input("Node name: ")
        g[node] = {}
        e = int(input(f"Enter no. of edges from {node}: "))
        for _ in range(e):
            nb, cost = input("Neighbor and cost (e.g. B 4): ").split()
            g[node][nb] = int(cost)
    return g

def bellman_ford(g, s):
    d = {n: float('inf') for n in g}; d[s] = 0
    for _ in range(len(g)-1):
        for u in g:
            for v,c in g[u].items():
                if d[u]+c < d[v]: d[v] = d[u]+c
    return d

def dijkstra(g, s):
    d = {n: float('inf') for n in g}; d[s]=0; vis=set()
    while len(vis)<len(g):
        u=min((n for n in g if n not in vis), key=lambda x:d[x])
        vis.add(u)
        for v,c in g[u].items():
            if d[u]+c<d[v]: d[v]=d[u]+c
    return d

g = get_graph()
s = input("Enter start node: ")

print("\n--- Distance Vector (Bellman-Ford) ---")
for n,d in bellman_ford(g,s).items(): print(f"{s}->{n}={d}")

print("\n--- Link State (Dijkstra) ---")
for n,d in dijkstra(g,s).items(): print(f"{s}->{n}={d}")

# Enter no. of nodes: 4
# Node name: A
# Enter no. of edges from A: 2
# Neighbor and cost (e.g. B 4): B 4
# Neighbor and cost (e.g. B 4): C 2
# Node name: B
# Enter no. of edges from B: 2
# Neighbor and cost (e.g. B 4): A 4
# Neighbor and cost (e.g. B 4): D 10
# Node name: C
# Enter no. of edges from C: 2
# Neighbor and cost (e.g. B 4): A 2
# Neighbor and cost (e.g. B 4): D 3
# Node name: D
# Enter no. of edges from D: 2
# Neighbor and cost (e.g. B 4): B 10
# Neighbor and cost (e.g. B 4): C 3
# Enter start node: A

