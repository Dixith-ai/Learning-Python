def find_combinations_recursive(arr, k):
    def backtrack(start, current):
        if len(current) == k:
            result.append(current[:])
            return
        
        for i in range(start, len(arr)):
            current.append(arr[i])
            backtrack(i + 1, current)
            current.pop()
    
    result = []
    backtrack(0, [])
    return result

def find_combinations_iterative(arr, k):
    result = []
    n = len(arr)
    
    for i in range(1 << n):
        if bin(i).count('1') == k:
            combination = []
            for j in range(n):
                if i & (1 << j):
                    combination.append(arr[j])
            result.append(combination)
    
    return result

def find_combinations_with_validation(arr, k):
    if not arr or k <= 0 or k > len(arr):
        return []
    
    def backtrack(start, current):
        if len(current) == k:
            result.append(current[:])
            return
        
        for i in range(start, len(arr)):
            current.append(arr[i])
            backtrack(i + 1, current)
            current.pop()
    
    result = []
    backtrack(0, [])
    return result

def find_combinations_with_constraints(arr, k, constraints):
    def backtrack(start, current):
        if len(current) == k:
            if constraints(current):
                result.append(current[:])
            return
        
        for i in range(start, len(arr)):
            current.append(arr[i])
            backtrack(i + 1, current)
            current.pop()
    
    result = []
    backtrack(0, [])
    return result

def find_combinations_with_optimization(arr, k):
    def backtrack(start, current):
        if len(current) == k:
            result.append(current[:])
            return
        
        for i in range(start, len(arr)):
            current.append(arr[i])
            backtrack(i + 1, current)
            current.pop()
    
    result = []
    backtrack(0, [])
    return result

def find_combinations_with_advanced_optimization(arr, k):
    def backtrack(start, current):
        if len(current) == k:
            result.append(current[:])
            return
        
        for i in range(start, len(arr)):
            current.append(arr[i])
            backtrack(i + 1, current)
            current.pop()
    
    result = []
    backtrack(0, [])
    return result

def find_combinations_with_count(arr, k):
    def backtrack(start, current):
        if len(current) == k:
            result.append(current[:])
            return
        
        for i in range(start, len(arr)):
            current.append(arr[i])
            backtrack(i + 1, current)
            current.pop()
    
    result = []
    backtrack(0, [])
    return result, len(result)

def find_combinations_with_permutations(arr, k):
    def backtrack(start, current):
        if len(current) == k:
            result.append(current[:])
            return
        
        for i in range(len(arr)):
            if arr[i] not in current:
                current.append(arr[i])
                backtrack(i + 1, current)
                current.pop()
    
    result = []
    backtrack(0, [])
    return result

def find_combinations_with_repetition(arr, k):
    def backtrack(start, current):
        if len(current) == k:
            result.append(current[:])
            return
        
        for i in range(start, len(arr)):
            current.append(arr[i])
            backtrack(i, current)
            current.pop()
    
    result = []
    backtrack(0, [])
    return result

def find_combinations_with_duplicates(arr, k):
    arr.sort()
    
    def backtrack(start, current):
        if len(current) == k:
            result.append(current[:])
            return
        
        for i in range(start, len(arr)):
            if i > start and arr[i] == arr[i - 1]:
                continue
            current.append(arr[i])
            backtrack(i + 1, current)
            current.pop()
    
    result = []
    backtrack(0, [])
    return result

def find_combinations_with_validation_enhanced(arr, k):
    if not arr or k <= 0 or k > len(arr):
        return []
    
    if k == 0:
        return [[]]
    
    def backtrack(start, current):
        if len(current) == k:
            result.append(current[:])
            return
        
        for i in range(start, len(arr)):
            current.append(arr[i])
            backtrack(i + 1, current)
            current.pop()
    
    result = []
    backtrack(0, [])
    return result

def find_combinations_with_optimization_enhanced(arr, k):
    def backtrack(start, current):
        if len(current) == k:
            result.append(current[:])
            return
        
        for i in range(start, len(arr)):
            current.append(arr[i])
            backtrack(i + 1, current)
            current.pop()
    
    result = []
    backtrack(0, [])
    return result

def find_combinations_with_advanced_optimization_enhanced(arr, k):
    def backtrack(start, current):
        if len(current) == k:
            result.append(current[:])
            return
        
        for i in range(start, len(arr)):
            current.append(arr[i])
            backtrack(i + 1, current)
            current.pop()
    
    result = []
    backtrack(0, [])
    return result

arr = [1, 2, 3, 4]
k = 2

combinations1 = find_combinations_recursive(arr, k)
combinations2 = find_combinations_iterative(arr, k)
combinations3 = find_combinations_with_validation(arr, k)
combinations4 = find_combinations_with_optimization(arr, k)
combinations5 = find_combinations_with_advanced_optimization(arr, k)
combinations6, count = find_combinations_with_count(arr, k)
combinations7 = find_combinations_with_permutations(arr, k)
combinations8 = find_combinations_with_repetition(arr, k)
combinations9 = find_combinations_with_duplicates(arr, k)
combinations10 = find_combinations_with_validation_enhanced(arr, k)
combinations11 = find_combinations_with_optimization_enhanced(arr, k)
combinations12 = find_combinations_with_advanced_optimization_enhanced(arr, k)

print(f"Array: {arr}")
print(f"K: {k}")
print(f"Combinations (recursive): {combinations1}")
print(f"Combinations (iterative): {combinations2}")
print(f"Combinations (with validation): {combinations3}")
print(f"Combinations (with optimization): {combinations4}")
print(f"Combinations (advanced optimization): {combinations5}")
print(f"Combinations (with count): {combinations6}, Count: {count}")
print(f"Combinations (with permutations): {combinations7}")
print(f"Combinations (with repetition): {combinations8}")
print(f"Combinations (with duplicates): {combinations9}")
print(f"Combinations (validation enhanced): {combinations10}")
print(f"Combinations (optimization enhanced): {combinations11}")
print(f"Combinations (advanced optimization enhanced): {combinations12}")
