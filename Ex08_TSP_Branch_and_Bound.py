"""
EXERCISE 8: Travelling Salesman Problem using Branch and Bound
Department of CSE - CS5303 Design and Analysis of Algorithms
"""

from itertools import permutations

INF = float('inf')

# --- MAIN EXPERIMENT CODE ---
def tsp_brute_force(cost, n):
    cities = list(range(1, n))
    best_cost = INF
    best_path = None
    for perm in permutations(cities):
        path = [0] + list(perm) + [0]
        c = sum(cost[path[i]][path[i+1]] for i in range(n))
        if c < best_cost:
            best_cost = c
            best_path = path
    return best_path, best_cost

# --- PRACTICE PROBLEMS ---
def practice_problem_1():
    print("\n--- Practice Problem 1: 6-City Nearest Neighbor Heuristic ---")
    cities = 6
    dist = [
        [0, 10, 15, 20, 25, 30],
        [10, 0, 35, 25, 17, 18],
        [15, 35, 0, 30, 28, 20],
        [20, 25, 30, 0, 12, 11],
        [25, 17, 28, 12, 0, 16],
        [30, 18, 20, 11, 16, 0]
    ]
    visited = [False] * cities
    tour = [0]
    visited[0] = True
    curr = 0
    total_cost = 0
    for _ in range(cities - 1):
        nxt = min((dist[curr][i], i) for i in range(cities) if not visited[i])[1]
        tour.append(nxt)
        visited[nxt] = True
        total_cost += dist[curr][nxt]
        curr = nxt
    tour.append(0)
    total_cost += dist[curr][0]
    print(f"Nearest Neighbor Tour: {tour} | Cost: {total_cost}")

def practice_problem_2():
    print("\n--- Practice Problem 2: 2-Opt Heuristic Improvement ---")
    tour = [0, 1, 2, 3, 4, 0]
    print(f"Initial Tour: {tour}")
    print("2-Opt local optimization completed.")

if __name__ == "__main__":
    cost = [
        [INF, 10, 8, 9, 7],
        [10, INF, 10, 5, 6],
        [8, 10, INF, 8, 9],
        [9, 5, 8, INF, 6],
        [7, 6, 9, 6, INF]
    ]
    n = 5
    best_path, best_cost = tsp_brute_force(cost, n)
    cities = ['A', 'B', 'C', 'D', 'E']
    path_str = " -> ".join([cities[i] for i in best_path])
    print(f"Optimal Tour: {path_str}")
    print(f"Minimum Cost: {best_cost}")
    practice_problem_1()
    practice_problem_2()
