"""
EXERCISE 6: Optimal Cost Computation in Matrix Chain Multiplication using DP
Department of CSE - CS5303 Design and Analysis of Algorithms
"""

# --- MAIN EXPERIMENT CODE ---
def matrix_chain_order(dims):
    n = len(dims) - 1
    m = [[0] * (n + 1) for _ in range(n + 1)]
    s = [[0] * (n + 1) for _ in range(n + 1)]
    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + dims[i - 1] * dims[k] * dims[j]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k
    return m, s

def print_optimal_parens(s, i, j):
    if i == j:
        return f"A{i}"
    k = s[i][j]
    left = print_optimal_parens(s, i, k)
    right = print_optimal_parens(s, k + 1, j)
    return f"({left} x {right})"

# --- PRACTICE PROBLEMS ---
def practice_problem_1():
    print("\n--- Practice Problem 1: Graphics Pipeline (5 Matrices) ---")
    dims = [4, 4, 4, 4, 10000, 1]
    m, s = matrix_chain_order(dims)
    print(f"Optimal Operations: {m[1][len(dims)-1]}")
    print(f"Optimal Order: {print_optimal_parens(s, 1, len(dims)-1)}")

def practice_problem_2():
    print("\n--- Practice Problem 2: Memoized Top-Down MCM ---")
    dims = [10, 20, 30, 40, 30, 10, 20]
    memo = {}
    def memoized_mcm(i, j):
        if i == j: return 0
        if (i, j) in memo: return memo[(i, j)]
        min_cost = float('inf')
        for k in range(i, j):
            cost = memoized_mcm(i, k) + memoized_mcm(k + 1, j) + dims[i - 1] * dims[k] * dims[j]
            min_cost = min(min_cost, cost)
        memo[(i, j)] = min_cost
        return min_cost

    cost = memoized_mcm(1, len(dims) - 1)
    print(f"Top-down Memoized Minimum Cost: {cost}")

if __name__ == "__main__":
    dims = [10, 30, 5, 60, 10]
    m, s = matrix_chain_order(dims)
    n = len(dims) - 1
    print(f"Minimum Scalar Multiplications: {m[1][n]}")
    print(f"Optimal Order: {print_optimal_parens(s, 1, n)}")
    practice_problem_1()
    practice_problem_2()
