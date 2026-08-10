"""
EXERCISE 2: Comparative Analysis of Naive, Rabin-Karp, and KMP Algorithms for String Matching
Department of CSE - CS5303 Design and Analysis of Algorithms
"""

import random

# --- MAIN EXPERIMENT CODE ---
def naive_search(text, pattern):
    n, m = len(text), len(pattern)
    matches, comparisons = [], 0
    for i in range(n - m + 1):
        j = 0
        while j < m:
            comparisons += 1
            if text[i + j] != pattern[j]:
                break
            j += 1
        if j == m:
            matches.append(i)
    return matches, comparisons

def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    length, i = 0, 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length != 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1
    return lps

def kmp_search(text, pattern):
    n, m = len(text), len(pattern)
    lps = compute_lps(pattern)
    matches, comparisons = [], 0
    i = j = 0
    while i < n:
        comparisons += 1
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            matches.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return matches, comparisons

def rabin_karp(text, pattern, q=101):
    n, m = len(text), len(pattern)
    d = 256
    h = pow(d, m - 1, q)
    p_hash = t_hash = 0
    matches, comparisons = [], 0
    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q
    for s in range(n - m + 1):
        if p_hash == t_hash:
            match = True
            for k in range(m):
                comparisons += 1
                if text[s + k] != pattern[k]:
                    match = False
                    break
            if match: matches.append(s)
        if s < n - m:
            t_hash = (d * (t_hash - ord(text[s]) * h) + ord(text[s + m])) % q
            if t_hash < 0: t_hash += q
    return matches, comparisons

# --- PRACTICE PROBLEMS ---
def practice_problem_1():
    print("\n--- Practice Problem 1: Manual KMP Trace ---")
    text = 'AABCAABXAAAZ'
    pattern = 'AABXAA'
    lps = compute_lps(pattern)
    matches, comps = kmp_search(text, pattern)
    print(f"Text: {text}")
    print(f"Pattern: {pattern}")
    print(f"Computed LPS Array: {lps}")
    print(f"Matches found at: {matches}, Comparisons: {comps}")

def practice_problem_2():
    print("\n--- Practice Problem 2: 2D Matrix Pattern Matching ---")
    text_matrix = [
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
        ['K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T'],
        ['U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D'],
        ['E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'],
        ['O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X'],
        ['Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
        ['I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R'],
        ['S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B'],
        ['C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'],
        ['M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V']
    ]
    pattern_matrix = [
        ['W', 'X', 'Y'],
        ['G', 'H', 'I'],
        ['Q', 'R', 'S']
    ]
    comps = 0
    matches = []
    R, C = 10, 10
    r, c = 3, 3
    for i in range(R - r + 1):
        for j in range(C - c + 1):
            match = True
            for pi in range(r):
                for pj in range(c):
                    comps += 1
                    if text_matrix[i + pi][j + pj] != pattern_matrix[pi][pj]:
                        match = False; break
                if not match: break
            if match: matches.append((i, j))
    print(f"2D Pattern Found at top-left positions: {matches}")
    print(f"Total Element Comparisons: {comps}")

if __name__ == "__main__":
    text = 'AABAACAADAABAABA'
    pattern = 'AABA'
    print(f"Text: {text}")
    print(f"Pattern: {pattern}")
    m1, c1 = naive_search(text, pattern)
    m2, c2 = kmp_search(text, pattern)
    m3, c3 = rabin_karp(text, pattern)
    print(f"Naive -> Matches: {m1}, Comparisons: {c1}")
    print(f"KMP   -> Matches: {m2}, Comparisons: {c2}")
    print(f"RK    -> Matches: {m3}, Comparisons: {c3}")
    practice_problem_1()
    practice_problem_2()
