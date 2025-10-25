def get_combinations(lst, r):
    if r == 0:
        return [[]]
    if not lst:
        return []
    
    combinations = []
    for i in range(len(lst)):
        current = lst[i]
        remaining = lst[i+1:]
        for combo in get_combinations(remaining, r-1):
            combinations.append([current] + combo)
    
    return combinations

def get_combinations_iterative(lst, r):
    from itertools import combinations
    return list(combinations(lst, r))

def get_all_combinations(lst):
    all_combos = []
    for r in range(len(lst) + 1):
        all_combos.extend(get_combinations(lst, r))
    return all_combos

def get_combinations_with_replacement(lst, r):
    from itertools import combinations_with_replacement
    return list(combinations_with_replacement(lst, r))

items = ['a', 'b', 'c']
r = 2

combos = get_combinations(items, r)
combos_iter = get_combinations_iterative(items, r)
all_combos = get_all_combinations(items)
combos_replacement = get_combinations_with_replacement(items, r)

print(f"Items: {items}")
print(f"Combinations of {r}: {combos}")
print(f"Combinations (iterative): {combos_iter}")
print(f"All combinations: {all_combos}")
print(f"Combinations with replacement: {combos_replacement}")
