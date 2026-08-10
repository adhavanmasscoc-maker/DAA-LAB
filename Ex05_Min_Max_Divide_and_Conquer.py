"""
EXERCISE 5: To Find Min-Max Value by Applying Divide and Conquer Technique
Department of CSE - CS5303 Design and Analysis of Algorithms
"""

import random

comparison_count = 0

# --- MAIN EXPERIMENT CODE ---
def min_max_dc(arr, low, high):
    global comparison_count
    if low == high:
        return arr[low], arr[low]
    if high == low + 1:
        comparison_count += 1
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        return arr[high], arr[low]
    
    mid = (low + high) // 2
    lmin, lmax = min_max_dc(arr, low, mid)
    rmin, rmax = min_max_dc(arr, mid + 1, high)
    
    comparison_count += 1
    overall_min = lmin if lmin < rmin else rmin
    comparison_count += 1
    overall_max = lmax if lmax > rmax else rmax
    return overall_min, overall_max

def min_max_naive(arr):
    mn, mx = arr[0], arr[0]
    comps = 0
    for x in arr[1:]:
        comps += 1
        if x < mn: mn = x
        comps += 1
        if x > mx: mx = x
    return mn, mx, comps

# --- PRACTICE PROBLEMS ---
def practice_problem_1():
    print("\n--- Practice Problem 1: Second Min and Second Max ---")
    arr = [12, 3, 5, 7, 19, 1, 8, 15]
    sorted_arr = sorted(set(arr))
    print(f"Array: {arr}")
    print(f"Min: {sorted_arr[0]}, 2nd Min: {sorted_arr[1]}")
    print(f"Max: {sorted_arr[-1]}, 2nd Max: {sorted_arr[-2]}")

def practice_problem_2():
    print("\n--- Practice Problem 2: QuickSelect (K-th Smallest Element) ---")
    def quickselect(arr, k):
        if len(arr) == 1: return arr[0]
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        if k <= len(left):
            return quickselect(left, k)
        elif k <= len(left) + len(middle):
            return middle[0]
        else:
            return quickselect(right, k - len(left) - len(middle))

    data = [random.randint(1, 10000) for _ in range(1000)]
    print(f"k=1 (Min): {quickselect(data, 1)}")
    print(f"k=500 (Median): {quickselect(data, 500)}")
    print(f"k=1000 (Max): {quickselect(data, 1000)}")

if __name__ == "__main__":
    arr = [3, 1, 7, 4, 9, 2, 8, 5, 6, 0]
    comparison_count = 0
    mn, mx = min_max_dc(arr, 0, len(arr) - 1)
    dc_comps = comparison_count
    _, _, naive_comps = min_max_naive(arr)
    print(f"Array: {arr}")
    print(f"Min: {mn}, Max: {mx}")
    print(f"D&C Comparisons: {dc_comps} | Naive Comparisons: {naive_comps}")
    practice_problem_1()
    practice_problem_2()
