"""
EXERCISE 9: Efficient Bin Packing using Approximation Algorithm
Department of CSE - CS5303 Design and Analysis of Algorithms
"""

# --- MAIN EXPERIMENT CODE ---
def first_fit(items, capacity=1.0):
    bins = []
    bin_contents = []
    for item in items:
        placed = False
        for i, space in enumerate(bins):
            if space >= item:
                bins[i] -= item
                bin_contents[i].append(item)
                placed = True; break
        if not placed:
            bins.append(capacity - item)
            bin_contents.append([item])
    return bin_contents

def first_fit_decreasing(items, capacity=1.0):
    return first_fit(sorted(items, reverse=True), capacity)

def best_fit_decreasing(items, capacity=1.0):
    sorted_items = sorted(items, reverse=True)
    bins = []
    bin_contents = []
    for item in sorted_items:
        best_idx = -1
        best_space = float('inf')
        for i, space in enumerate(bins):
            if space >= item and space - item < best_space:
                best_space = space - item
                best_idx = i
        if best_idx >= 0:
            bins[best_idx] -= item
            bin_contents[best_idx].append(item)
        else:
            bins.append(capacity - item)
            bin_contents.append([item])
    return bin_contents

# --- PRACTICE PROBLEMS ---
def practice_problem_1():
    print("\n--- Practice Problem 1: Cloud Server Allocation (8GB Capacity) ---")
    tasks = [1.5, 2.0, 3.5, 0.5, 4.0, 1.0, 2.5, 3.0, 1.5, 2.0, 0.5, 4.0, 1.0, 3.5, 2.0]
    ffd_bins = first_fit_decreasing(tasks, capacity=8.0)
    bfd_bins = best_fit_decreasing(tasks, capacity=8.0)
    print(f"FFD Servers Needed: {len(ffd_bins)}")
    print(f"BFD Servers Needed: {len(bfd_bins)}")

def practice_problem_2():
    print("\n--- Practice Problem 2: Next Fit Decreasing (NFD) ---")
    def next_fit_decreasing(items, capacity=1.0):
        items = sorted(items, reverse=True)
        bins = []
        curr_space = 0
        for item in items:
            if item <= curr_space:
                curr_space -= item
            else:
                bins.append(1)
                curr_space = capacity - item
        return len(bins)

    items = [0.5, 0.7, 0.3, 0.9, 0.2, 0.6, 0.8, 0.4, 0.1, 0.5]
    print(f"NFD Bins Used: {next_fit_decreasing(items)}")

if __name__ == "__main__":
    items = [0.5, 0.7, 0.3, 0.9, 0.2, 0.6, 0.8, 0.4, 0.1, 0.5]
    print(f"FF Bins:  {len(first_fit(items))}")
    print(f"FFD Bins: {len(first_fit_decreasing(items))}")
    print(f"BFD Bins: {len(best_fit_decreasing(items))}")
    practice_problem_1()
    practice_problem_2()
