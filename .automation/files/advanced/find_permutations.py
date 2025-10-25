def find_permutations_recursive(arr):
    if len(arr) <= 1:
        return [arr]
    
    result = []
    for i in range(len(arr)):
        rest = arr[:i] + arr[i+1:]
        for perm in find_permutations_recursive(rest):
            result.append([arr[i]] + perm)
    
    return result

def find_permutations_backtracking(arr):
    result = []
    
    def backtrack(current):
        if len(current) == len(arr):
            result.append(current[:])
            return
        
        for num in arr:
            if num not in current:
                current.append(num)
                backtrack(current)
                current.pop()
    
    backtrack([])
    return result

def find_permutations_iterative(arr):
    from itertools import permutations
    return list(permutations(arr))

def find_permutations_heap(arr):
    def heap_permute(n):
        if n == 1:
            yield arr[:]
        else:
            for i in range(n):
                yield from heap_permute(n - 1)
                if n % 2 == 1:
                    arr[0], arr[n - 1] = arr[n - 1], arr[0]
                else:
                    arr[i], arr[n - 1] = arr[n - 1], arr[i]
    
    return list(heap_permute(len(arr)))

def find_permutations_lexicographic(arr):
    arr = sorted(arr)
    result = [arr[:]]
    
    while True:
        i = len(arr) - 1
        while i > 0 and arr[i - 1] >= arr[i]:
            i -= 1
        
        if i == 0:
            break
        
        j = len(arr) - 1
        while arr[j] <= arr[i - 1]:
            j -= 1
        
        arr[i - 1], arr[j] = arr[j], arr[i - 1]
        arr[i:] = arr[i:][::-1]
        result.append(arr[:])
    
    return result

def find_permutations_with_duplicates(arr):
    from collections import Counter
    
    def backtrack(current, counter):
        if len(current) == len(arr):
            result.append(current[:])
            return
        
        for num in counter:
            if counter[num] > 0:
                current.append(num)
                counter[num] -= 1
                backtrack(current, counter)
                counter[num] += 1
                current.pop()
    
    result = []
    counter = Counter(arr)
    backtrack([], counter)
    return result

def find_permutations_with_constraints(arr, constraints):
    def is_valid(current):
        for constraint in constraints:
            if not constraint(current):
                return False
        return True
    
    def backtrack(current):
        if len(current) == len(arr):
            result.append(current[:])
            return
        
        for num in arr:
            if num not in current:
                current.append(num)
                if is_valid(current):
                    backtrack(current)
                current.pop()
    
    result = []
    backtrack([])
    return result

def find_permutations_with_validation(arr):
    if not arr:
        return []
    
    if len(arr) == 1:
        return [arr]
    
    result = []
    for i in range(len(arr)):
        rest = arr[:i] + arr[i+1:]
        for perm in find_permutations_with_validation(rest):
            result.append([arr[i]] + perm)
    
    return result

def find_permutations_with_optimization(arr):
    if len(arr) <= 1:
        return [arr]
    
    result = []
    used = set()
    
    def backtrack(current):
        if len(current) == len(arr):
            result.append(current[:])
            return
        
        for num in arr:
            if num not in used:
                used.add(num)
                current.append(num)
                backtrack(current)
                current.pop()
                used.remove(num)
    
    backtrack([])
    return result

def find_permutations_with_count(arr):
    def count_permutations(n):
        if n <= 1:
            return 1
        return n * count_permutations(n - 1)
    
    total_count = count_permutations(len(arr))
    result = []
    
    def backtrack(current):
        if len(current) == len(arr):
            result.append(current[:])
            return
        
        for num in arr:
            if num not in current:
                current.append(num)
                backtrack(current)
                current.pop()
    
    backtrack([])
    return result, total_count

arr = [1, 2, 3]

perms1 = find_permutations_recursive(arr)
perms2 = find_permutations_backtracking(arr)
perms3 = find_permutations_iterative(arr)
perms4 = find_permutations_heap(arr[:])
perms5 = find_permutations_lexicographic(arr[:])
perms6 = find_permutations_with_duplicates([1, 1, 2])
perms7 = find_permutations_with_validation(arr)
perms8 = find_permutations_with_optimization(arr)
perms9, count = find_permutations_with_count(arr)

print(f"Array: {arr}")
print(f"Permutations (recursive): {perms1}")
print(f"Permutations (backtracking): {perms2}")
print(f"Permutations (iterative): {perms3}")
print(f"Permutations (heap): {perms4}")
print(f"Permutations (lexicographic): {perms5}")
print(f"Permutations (with duplicates): {perms6}")
print(f"Permutations (with validation): {perms7}")
print(f"Permutations (with optimization): {perms8}")
print(f"Permutations (with count): {perms9}, Count: {count}")
