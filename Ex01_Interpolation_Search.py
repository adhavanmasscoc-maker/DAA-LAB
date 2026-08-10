"""
EXERCISE 1: Implementation and Performance Analysis of Interpolation Search
Department of CSE - CS5303 Design and Analysis of Algorithms
"""

import time
import random

# --- MAIN EXPERIMENT CODE ---
def interpolation_search(arr, target):
    """Interpolation Search Algorithm"""
    low, high = 0, len(arr) - 1
    comparisons = 0
    while low <= high and arr[low] <= target <= arr[high]:
        comparisons += 1
        if low == high:
            if arr[low] == target:
                return low, comparisons
            return -1, comparisons
        
        pos = low + int(((target - arr[low]) * (high - low)) / (arr[high] - arr[low]))
        if arr[pos] == target:
            return pos, comparisons
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1, comparisons

def binary_search(arr, target):
    """Binary Search Algorithm"""
    low, high = 0, len(arr) - 1
    comparisons = 0
    while low <= high:
        comparisons += 1
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, comparisons

def performance_analysis():
    sizes = [1000, 5000, 10000, 50000, 100000]
    print(f"\n{'Size':>10} {'IS Time(ms)':>14} {'BS Time(ms)':>14} {'IS Comparisons':>16} {'BS Comparisons':>16}")
    print('-'*75)
    for size in sizes:
        arr = sorted(random.sample(range(size * 10), size))
        target = arr[random.randint(0, size - 1)]
        
        start = time.perf_counter()
        for _ in range(100):
            idx_is, comp_is = interpolation_search(arr, target)
        is_time = ((time.perf_counter() - start) / 100) * 1000

        start = time.perf_counter()
        for _ in range(100):
            idx_bs, comp_bs = binary_search(arr, target)
        bs_time = ((time.perf_counter() - start) / 100) * 1000

        print(f"{size:>10} {is_time:>14.4f} {bs_time:>14.4f} {comp_is:>16} {comp_bs:>16}")

# --- PRACTICE PROBLEMS ---
def practice_problem_1():
    print("\n--- Practice Problem 1: Roll Numbers Search ---")
    roll_numbers = sorted(random.sample(range(1, 10001), 5000))
    target = roll_numbers[len(roll_numbers) // 2]
    idx_is, comp_is = interpolation_search(roll_numbers, target)
    idx_bs, comp_bs = binary_search(roll_numbers, target)
    print(f"Searching for Roll No {target}:")
    print(f"Interpolation Search -> Probes/Comps: {comp_is}")
    print(f"Binary Search -> Probes/Comps: {comp_bs}")

def practice_problem_2():
    print("\n--- Practice Problem 2: Floating-Point Interpolation Search ---")
    def interpolation_search_float(arr, target):
        low, high = 0, len(arr) - 1
        comparisons = 0
        while low <= high and arr[low] <= target <= arr[high]:
            comparisons += 1
            if arr[high] == arr[low]:
                if arr[low] == target: return low, comparisons
                break
            pos = low + int(((target - arr[low]) * (high - low)) / (arr[high] - arr[low]))
            if pos < low or pos > high: break
            if arr[pos] == target: return pos, comparisons
            elif arr[pos] < target: low = pos + 1
            else: high = pos - 1
        return -1, comparisons

    for size in [10000, 50000, 100000]:
        arr = sorted([random.uniform(0.0, 1000.0) for _ in range(size)])
        target = arr[size // 2]
        _, comps = interpolation_search_float(arr, target)
        print(f"Dataset Size: {size:>6} | Float Interpolation Search Comparisons: {comps}")

if __name__ == "__main__":
    arr = [2, 5, 10, 15, 23, 35, 48, 60, 75, 90, 105, 120]
    target = 35
    idx, comps = interpolation_search(arr, target)
    print(f"Array: {arr}")
    print(f"Searching for: {target}")
    print(f"Found at index: {idx}, Comparisons: {comps}")
    performance_analysis()
    practice_problem_1()
    practice_problem_2()
