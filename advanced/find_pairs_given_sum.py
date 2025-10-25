def find_pairs_brute_force(arr, target):
    pairs = []
    
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                pairs.append((arr[i], arr[j]))
    
    return pairs

def find_pairs_hashmap(arr, target):
    pairs = []
    seen = set()
    
    for num in arr:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    
    return pairs

def find_pairs_optimized(arr, target):
    pairs = []
    seen = set()
    
    for num in arr:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    
    return pairs

def find_pairs_with_validation(arr, target):
    if not arr or len(arr) < 2:
        return []
    
    pairs = []
    seen = set()
    
    for num in arr:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    
    return pairs

def find_pairs_with_constraints(arr, target, constraints):
    pairs = []
    seen = set()
    
    for num in arr:
        if constraints(num):
            complement = target - num
            if complement in seen:
                pairs.append((complement, num))
            seen.add(num)
    
    return pairs

def find_pairs_with_optimization(arr, target):
    pairs = []
    seen = set()
    
    for num in arr:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    
    return pairs

def find_pairs_with_advanced_optimization(arr, target):
    pairs = []
    seen = set()
    
    for num in arr:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    
    return pairs

def find_pairs_with_count(arr, target):
    pairs = []
    seen = set()
    count = 0
    
    for num in arr:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
            count += 1
        seen.add(num)
    
    return pairs, count

def find_pairs_with_indices(arr, target):
    pairs = []
    seen = {}
    
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            pairs.append((seen[complement], i))
        seen[num] = i
    
    return pairs

def find_pairs_with_negative(arr, target):
    pairs = []
    seen = set()
    
    for num in arr:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    
    return pairs

def find_pairs_with_circular(arr, target):
    pairs = []
    seen = set()
    
    for i in range(2 * len(arr)):
        num = arr[i % len(arr)]
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    
    return pairs

def find_pairs_with_validation_enhanced(arr, target):
    if not arr or len(arr) < 2:
        return []
    
    if target == 0:
        return []
    
    pairs = []
    seen = set()
    
    for num in arr:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    
    return pairs

def find_pairs_with_optimization_enhanced(arr, target):
    pairs = []
    seen = set()
    
    for num in arr:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    
    return pairs

def find_pairs_with_advanced_optimization_enhanced(arr, target):
    pairs = []
    seen = set()
    
    for num in arr:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    
    return pairs

def find_pairs_with_statistics(arr, target):
    pairs = []
    seen = set()
    count = 0
    sum_pairs = 0
    
    for num in arr:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
            count += 1
            sum_pairs += complement + num
        seen.add(num)
    
    return pairs, count, sum_pairs

def find_pairs_with_advanced_features(arr, target):
    pairs = []
    seen = set()
    count = 0
    sum_pairs = 0
    min_pair = None
    max_pair = None
    
    for num in arr:
        complement = target - num
        if complement in seen:
            pair = (complement, num)
            pairs.append(pair)
            count += 1
            sum_pairs += complement + num
            
            if min_pair is None or complement + num < min_pair[0] + min_pair[1]:
                min_pair = pair
            
            if max_pair is None or complement + num > max_pair[0] + max_pair[1]:
                max_pair = pair
        
        seen.add(num)
    
    return pairs, count, sum_pairs, min_pair, max_pair

arr = [2, 7, 11, 15, 3, 6]
target = 9

pairs1 = find_pairs_brute_force(arr, target)
pairs2 = find_pairs_hashmap(arr, target)
pairs3 = find_pairs_optimized(arr, target)
pairs4 = find_pairs_with_validation(arr, target)
pairs5 = find_pairs_with_optimization(arr, target)
pairs6 = find_pairs_with_advanced_optimization(arr, target)
pairs7, count = find_pairs_with_count(arr, target)
pairs8 = find_pairs_with_indices(arr, target)
pairs9 = find_pairs_with_negative(arr, target)
pairs10 = find_pairs_with_circular(arr, target)
pairs11 = find_pairs_with_validation_enhanced(arr, target)
pairs12 = find_pairs_with_optimization_enhanced(arr, target)
pairs13 = find_pairs_with_advanced_optimization_enhanced(arr, target)
pairs14, count2, sum_pairs = find_pairs_with_statistics(arr, target)
pairs15, count3, sum_pairs2, min_pair, max_pair = find_pairs_with_advanced_features(arr, target)

print(f"Array: {arr}")
print(f"Target: {target}")
print(f"Pairs (brute force): {pairs1}")
print(f"Pairs (hashmap): {pairs2}")
print(f"Pairs (optimized): {pairs3}")
print(f"Pairs (with validation): {pairs4}")
print(f"Pairs (with optimization): {pairs5}")
print(f"Pairs (advanced optimization): {pairs6}")
print(f"Pairs (with count): {pairs7}, Count: {count}")
print(f"Pairs (with indices): {pairs8}")
print(f"Pairs (with negative): {pairs9}")
print(f"Pairs (with circular): {pairs10}")
print(f"Pairs (validation enhanced): {pairs11}")
print(f"Pairs (optimization enhanced): {pairs12}")
print(f"Pairs (advanced optimization enhanced): {pairs13}")
print(f"Pairs (with statistics): {pairs14}, Count: {count2}, Sum: {sum_pairs}")
print(f"Pairs (with advanced features): {pairs15}, Count: {count3}, Sum: {sum_pairs2}, Min: {min_pair}, Max: {max_pair}")
