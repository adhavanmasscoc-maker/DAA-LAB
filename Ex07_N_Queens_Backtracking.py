"""
EXERCISE 7: Solving N-Queens Problem using Backtracking
Department of CSE - CS5303 Design and Analysis of Algorithms
"""

# --- MAIN EXPERIMENT CODE ---
def is_safe(board, row, col):
    for prev_row in range(row):
        placed = board[prev_row]
        if placed == col or abs(prev_row - row) == abs(placed - col):
            return False
    return True

def solve_n_queens(n):
    board = [-1] * n
    solutions = []
    backtrack_count = [0]

    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1
            backtrack_count[0] += 1

    backtrack(0)
    return solutions, backtrack_count[0]

# --- PRACTICE PROBLEMS ---
def practice_problem_1():
    print("\n--- Practice Problem 1: Bitmask N-Queens (N=12) ---")
    def solve_bitmask(n):
        count = [0]
        def backtrack(row, cols, diag1, diag2):
            if row == n:
                count[0] += 1
                return
            available = ((1 << n) - 1) & ~(cols | diag1 | diag2)
            while available:
                p = available & -available
                available &= available - 1
                backtrack(row + 1, cols | p, (diag1 | p) << 1, (diag2 | p) >> 1)
        backtrack(0, 0, 0, 0)
        return count[0]

    n = 12
    solutions = solve_bitmask(n)
    print(f"Bitmask N-Queens N={n} total solutions found: {solutions}")

def practice_problem_2():
    print("\n--- Practice Problem 2: Knight's Tour (8x8) ---")
    N = 8
    board = [[-1] * N for _ in range(N)]
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]
    board[0][0] = 0

    def solve_kt(x, y, pos):
        if pos == N * N: return True
        for i in range(8):
            nx, ny = x + move_x[i], y + move_y[i]
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == -1:
                board[nx][ny] = pos
                if solve_kt(nx, ny, pos + 1): return True
                board[nx][ny] = -1
        return False

    solve_kt(0, 0, 1)
    print("Knight's Tour (First 4 rows preview):")
    for row in board[:4]:
        print(row)

if __name__ == "__main__":
    for n in [4, 6, 8]:
        sols, backtracks = solve_n_queens(n)
        print(f"N={n}: {len(sols)} solutions, {backtracks} backtracks")
    practice_problem_1()
    practice_problem_2()
