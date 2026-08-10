"""
EXERCISE 10: Improving Quick Sort Efficiency using Randomized Algorithm
Department of CSE - CS5303 Design and Analysis of Algorithms
"""

import random
import sys
sys.setrecursionlimit(20000)

comparisons = 0

# --- MAIN EXPERIMENT CODE ---
def partition(arr, low, high):
    global comparisons
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        comparisons += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def deterministic_quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        deterministic_quicksort(arr, low, pi - 1)
        deterministic_quicksort(arr, pi + 1, high)

def randomized_quicksort(arr, low, high):
    if low < high:
        rand_idx = random.randint(low, high)
        arr[rand_idx], arr[high] = arr[high], arr[rand_idx]
        pi = partition(arr, low, high)
        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)

# --- PRACTICE PROBLEMS ---
def practice_problem_1():
    print("\n--- Practice Problem 1: Median-of-Three QuickSort ---")
    def median_of_three(arr, low, high):
        mid = (low + high) // 2
        candidates = [(arr[low], low), (arr[mid], mid), (arr[high], high)]
        candidates.sort()
        return candidates[1][1]

    arr = [9, 2, 7, 1, 5, 8, 3, 6]
    m_idx = median_of_three(arr, 0, len(arr) - 1)
    print(f"Array: {arr}")
    print(f"Median of Three Pivot Selected: {arr[m_idx]}")

def practice_problem_2():
    print("\n--- Practice Problem 2: IntroSort Hybrid ---")
    print("IntroSort switches to HeapSort if depth exceeds 2 * log2(n).")

if __name__ == "__main__":
    arr_d = [random.randint(1, 1000) for _ in range(100)]
    arr_r = arr_d[:]
    
    comparisons = 0
    deterministic_quicksort(arr_d, 0, len(arr_d) - 1)
    comps_d = comparisons

    comparisons = 0
    randomized_quicksort(arr_r, 0, len(arr_r) - 1)
    comps_r = comparisons

    print(f"Deterministic QuickSort Comparisons: {comps_d}")
    print(f"Randomized QuickSort Comparisons:    {comps_r}")
    practice_problem_1()
    practice_problem_2()
