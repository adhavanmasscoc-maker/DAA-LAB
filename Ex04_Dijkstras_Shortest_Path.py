"""
EXERCISE 4: Implementation of Single Source Shortest Path Algorithm (Dijkstra's)
Department of CSE - CS5303 Design and Analysis of Algorithms
"""

import heapq

# --- MAIN EXPERIMENT CODE ---
def dijkstra(graph, source):
    n = len(graph)
    dist = [float('inf')] * n
    prev = [None] * n
    dist[source] = 0
    pq = [(0, source)]
    visited = set()
    while pq:
        d, u = heapq.heappop(pq)
        if u in visited: continue
        visited.add(u)
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))
    return dist, prev

def reconstruct_path(prev, source, target):
    path = []
    node = target
    while node is not None:
        path.append(node)
        node = prev[node]
    path.reverse()
    return path if path[0] == source else []

# --- PRACTICE PROBLEMS ---
def practice_problem_1():
    print("\n--- Practice Problem 1: City Road Network (Airport to Station) ---")
    graph = {
        0: [(1, 10), (2, 5)],
        1: [(3, 1), (2, 2)],
        2: [(1, 3), (3, 9), (4, 2)],
        3: [(4, 4)],
        4: []
    }
    dist, prev = dijkstra(graph, 0)
    path = reconstruct_path(prev, 0, 4)
    print(f"Fastest Route (0 -> 4): {' -> '.join(map(str, path))} | Time: {dist[4]} mins")

def practice_problem_2():
    print("\n--- Practice Problem 2: Modified Dijkstra with Hop Count ---")
    def dijkstra_hops(graph, source):
        n = len(graph)
        dist = [float('inf')] * n
        hops = [float('inf')] * n
        prev = [None] * n
        dist[source] = 0
        hops[source] = 0
        pq = [(0, 0, source)]
        while pq:
            d, h, u = heapq.heappop(pq)
            for v, w in graph[u]:
                if dist[u] + w < dist[v] or (dist[u] + w == dist[v] and hops[u] + 1 < hops[v]):
                    dist[v] = dist[u] + w
                    hops[v] = hops[u] + 1
                    prev[v] = u
                    heapq.heappush(pq, (dist[v], hops[v], v))
        return dist, hops, prev

    graph = {
        0: [(1, 4), (2, 2)],
        1: [(3, 2)],
        2: [(1, 1), (3, 4)],
        3: [(4, 3)],
        4: [(5, 1)],
        5: []
    }
    dist, hops, prev = dijkstra_hops(graph, 0)
    print(f"Shortest distance to node 5: {dist[5]} with {hops[5]} hops")

if __name__ == "__main__":
    graph = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: [(4, 3)],
        4: [(5, 2)],
        5: []
    }
    source = 0
    dist, prev = dijkstra(graph, source)
    print(f"Shortest paths from vertex {source}:")
    for v in range(len(graph)):
        p = reconstruct_path(prev, source, v)
        print(f"Vertex {v}: Distance = {dist[v]}, Path = {p}")
    practice_problem_1()
    practice_problem_2()
