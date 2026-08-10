"""
EXERCISE 3: Implementation of Kruskal's and Prim's Algorithms for Minimum Spanning Tree
Department of CSE - CS5303 Design and Analysis of Algorithms
"""

import heapq

# --- MAIN EXPERIMENT CODE ---
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry: return False
        if self.rank[rx] < self.rank[ry]: rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]: self.rank[rx] += 1
        return True

def kruskal(n, edges):
    edges.sort()
    uf = UnionFind(n)
    mst, cost = [], 0
    for w, u, v in edges:
        if uf.union(u, v):
            mst.append((u, v, w))
            cost += w
            if len(mst) == n - 1: break
    return mst, cost

def prim(n, adj, start=0):
    INF = float('inf')
    key = [INF] * n
    inMST = [False] * n
    parent = [-1] * n
    key[start] = 0
    pq = [(0, start)]
    mst, cost = [], 0
    while pq:
        w, u = heapq.heappop(pq)
        if inMST[u]: continue
        inMST[u] = True
        if parent[u] != -1:
            mst.append((parent[u], u, w))
            cost += w
        for v, wt in adj.get(u, []):
            if not inMST[v] and wt < key[v]:
                key[v] = wt
                parent[v] = u
                heapq.heappush(pq, (wt, v))
    return mst, cost

# --- PRACTICE PROBLEMS ---
def practice_problem_1():
    print("\n--- Practice Problem 1: 6-City Kruskal's MST ---")
    cities = ['A', 'B', 'C', 'D', 'E', 'F']
    mapping = {c: i for i, c in enumerate(cities)}
    edges = [
        (4, mapping['A'], mapping['B']), (2, mapping['A'], mapping['C']),
        (5, mapping['B'], mapping['C']), (10, mapping['B'], mapping['D']),
        (3, mapping['C'], mapping['E']), (7, mapping['D'], mapping['E']),
        (8, mapping['D'], mapping['F']), (6, mapping['E'], mapping['F'])
    ]
    mst, cost = kruskal(6, edges)
    print("MST Edges:")
    for u, v, w in mst:
        print(f"  {cities[u]} - {cities[v]} : {w}")
    print(f"Total Cost: {cost}")

def practice_problem_2():
    print("\n--- Practice Problem 2: Prim's Adjacency Matrix O(V^2) ---")
    def prim_matrix(n, adj_matrix):
        key = [float('inf')] * n
        parent = [-1] * n
        inMST = [False] * n
        key[0] = 0
        for _ in range(n):
            u = min((k, i) for i, k in enumerate(key) if not inMST[i])[1]
            inMST[u] = True
            for v in range(n):
                if adj_matrix[u][v] > 0 and not inMST[v] and adj_matrix[u][v] < key[v]:
                    key[v] = adj_matrix[u][v]
                    parent[v] = u
        return sum(key)

    n = 100
    adj_matrix = [[0 if i == j else (i + j) % 20 + 1 for j in range(n)] for i in range(n)]
    cost = prim_matrix(n, adj_matrix)
    print(f"Dense Graph (100 Nodes) Prim's MST Cost: {cost}")

if __name__ == "__main__":
    n = 7
    edges = [(7,0,1),(5,0,3),(8,1,2),(9,1,3),(7,1,4),(5,2,4),(15,3,4),(6,3,5),(8,4,5),(9,4,6),(11,5,6)]
    adj = {}
    for w, u, v in edges:
        adj.setdefault(u, []).append((v, w))
        adj.setdefault(v, []).append((u, w))

    kmst, k_cost = kruskal(n, edges[:])
    pmst, p_cost = prim(n, adj)
    print(f"=== Kruskal's Total Cost: {k_cost} ===")
    print(f"=== Prim's Total Cost: {p_cost} ===")
    practice_problem_1()
    practice_problem_2()
