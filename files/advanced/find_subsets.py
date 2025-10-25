def find_subsets_recursive(arr):
    if not arr:
        return [[]]
    
    first = arr[0]
    rest = arr[1:]
    subsets_without_first = find_subsets_recursive(rest)
    subsets_with_first = [[first] + subset for subset in subsets_without_first]
    
    return subsets_without_first + subsets_with_first

def find_subsets_backtracking(arr):
    result = []
    
    def backtrack(start, current):
        result.append(current[:])
        
        for i in range(start, len(arr)):
            current.append(arr[i])
            backtrack(i + 1, current)
            current.pop()
    
    backtrack(0, [])
    return result

def find_subsets_iterative(arr):
    result = [[]]
    
    for num in arr:
        result.extend([subset + [num] for subset in result])
    
    return result

def find_subsets_bit_manipulation(arr):
    n = len(arr)
    result = []
    
    for i in range(1 << n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(arr[j])
        result.append(subset)
    
    return result

def find_subsets_with_length(arr, length):
    result = []
    
    def backtrack(start, current):
        if len(current) == length:
            result.append(current[:])
            return
        
        for i in range(start, len(arr)):
            current.append(arr[i])
            backtrack(i + 1, current)
            current.pop()
    
    backtrack(0, [])
    return result

def find_subsets_with_sum(arr, target_sum):
    result = []
    
    def backtrack(start, current, current_sum):
        if current_sum == target_sum:
            result.append(current[:])
            return
        
        for i in range(start, len(arr)):
            if current_sum + arr[i] <= target_sum:
                current.append(arr[i])
                backtrack(i + 1, current, current_sum + arr[i])
                current.pop()
    
    backtrack(0, [], 0)
    return result

def find_subsets_with_constraints(arr, constraints):
    result = []
    
    def is_valid(subset):
        for constraint in constraints:
            if not constraint(subset):
                return False
        return True
    
    def backtrack(start, current):
        if is_valid(current):
            result.append(current[:])
        
        for i in range(start, len(arr)):
            current.append(arr[i])
            backtrack(i + 1, current)
            current.pop()
    
    backtrack(0, [])
    return result

def find_subsets_with_duplicates(arr):
    from collections import Counter
    
    def backtrack(start, current, counter):
        result.append(current[:])
        
        for i in range(start, len(arr)):
            if counter[arr[i]] > 0:
                current.append(arr[i])
                counter[arr[i]] -= 1
                backtrack(i, current, counter)
                counter[arr[i]] += 1
                current.pop()
    
    result = []
    counter = Counter(arr)
    backtrack(0, [], counter)
    return result

def find_subsets_with_validation(arr):
    if not arr:
        return [[]]
    
    if len(arr) == 1:
        return [[], [arr[0]]]
    
    first = arr[0]
    rest = arr[1:]
    subsets_without_first = find_subsets_with_validation(rest)
    subsets_with_first = [[first] + subset for subset in subsets_without_first]
    
    return subsets_without_first + subsets_with_first

def find_subsets_with_optimization(arr):
    result = []
    
    def backtrack(start, current):
        result.append(current[:])
        
        for i in range(start, len(arr)):
            current.append(arr[i])
            backtrack(i + 1, current)
            current.pop()
    
    backtrack(0, [])
    return result

def find_subsets_with_count(arr):
    def count_subsets(n):
        return 2 ** n
    
    total_count = count_subsets(len(arr))
    result = []
    
    def backtrack(start, current):
        result.append(current[:])
        
        for i in range(start, len(arr)):
            current.append(arr[i])
            backtrack(i + 1, current)
            current.pop()
    
    backtrack(0, [])
    return result, total_count

def find_subsets_with_odd_even(arr):
    odd_subsets = []
    even_subsets = []
    
    def backtrack(start, current):
        if len(current) % 2 == 0:
            even_subsets.append(current[:])
        else:
            odd_subsets.append(current[:])
        
        for i in range(start, len(arr)):
            current.append(arr[i])
            backtrack(i + 1, current)
            current.pop()
    
    backtrack(0, [])
    return odd_subsets, even_subsets

arr = [1, 2, 3]

subsets1 = find_subsets_recursive(arr)
subsets2 = find_subsets_backtracking(arr)
subsets3 = find_subsets_iterative(arr)
subsets4 = find_subsets_bit_manipulation(arr)
subsets5 = find_subsets_with_length(arr, 2)
subsets6 = find_subsets_with_sum(arr, 3)
subsets7 = find_subsets_with_validation(arr)
subsets8 = find_subsets_with_optimization(arr)
subsets9, count = find_subsets_with_count(arr)
subsets10, even_subsets = find_subsets_with_odd_even(arr)

print(f"Array: {arr}")
print(f"Subsets (recursive): {subsets1}")
print(f"Subsets (backtracking): {subsets2}")
print(f"Subsets (iterative): {subsets3}")
print(f"Subsets (bit manipulation): {subsets4}")
print(f"Subsets (length 2): {subsets5}")
print(f"Subsets (sum 3): {subsets6}")
print(f"Subsets (with validation): {subsets7}")
print(f"Subsets (with optimization): {subsets8}")
print(f"Subsets (with count): {subsets9}, Count: {count}")
print(f"Odd subsets: {subsets10}")
print(f"Even subsets: {even_subsets}")
