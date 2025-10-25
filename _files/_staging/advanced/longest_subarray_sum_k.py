def longest_subarray_sum_k_brute_force(arr, k):
    max_length = 0
    
    for i in range(len(arr)):
        current_sum = 0
        for j in range(i, len(arr)):
            current_sum += arr[j]
            if current_sum == k:
                max_length = max(max_length, j - i + 1)
    
    return max_length

def longest_subarray_sum_k_hashmap(arr, k):
    prefix_sum = {0: -1}
    max_length = 0
    current_sum = 0
    
    for i in range(len(arr)):
        current_sum += arr[i]
        
        if current_sum - k in prefix_sum:
            max_length = max(max_length, i - prefix_sum[current_sum - k])
        
        if current_sum not in prefix_sum:
            prefix_sum[current_sum] = i
    
    return max_length

def longest_subarray_sum_k_optimized(arr, k):
    prefix_sum = {0: -1}
    max_length = 0
    current_sum = 0
    
    for i in range(len(arr)):
        current_sum += arr[i]
        
        if current_sum - k in prefix_sum:
            max_length = max(max_length, i - prefix_sum[current_sum - k])
        
        if current_sum not in prefix_sum:
            prefix_sum[current_sum] = i
    
    return max_length

def longest_subarray_sum_k_with_validation(arr, k):
    if not arr:
        return 0
    
    if k == 0:
        return 0
    
    prefix_sum = {0: -1}
    max_length = 0
    current_sum = 0
    
    for i in range(len(arr)):
        current_sum += arr[i]
        
        if current_sum - k in prefix_sum:
            max_length = max(max_length, i - prefix_sum[current_sum - k])
        
        if current_sum not in prefix_sum:
            prefix_sum[current_sum] = i
    
    return max_length

def longest_subarray_sum_k_with_constraints(arr, k, constraints):
    prefix_sum = {0: -1}
    max_length = 0
    current_sum = 0
    
    for i in range(len(arr)):
        if constraints(arr[i]):
            current_sum += arr[i]
            
            if current_sum - k in prefix_sum:
                max_length = max(max_length, i - prefix_sum[current_sum - k])
            
            if current_sum not in prefix_sum:
                prefix_sum[current_sum] = i
    
    return max_length

def longest_subarray_sum_k_with_optimization(arr, k):
    prefix_sum = {0: -1}
    max_length = 0
    current_sum = 0
    
    for i in range(len(arr)):
        current_sum += arr[i]
        
        if current_sum - k in prefix_sum:
            max_length = max(max_length, i - prefix_sum[current_sum - k])
        
        if current_sum not in prefix_sum:
            prefix_sum[current_sum] = i
    
    return max_length

def longest_subarray_sum_k_with_advanced_optimization(arr, k):
    prefix_sum = {0: -1}
    max_length = 0
    current_sum = 0
    
    for i in range(len(arr)):
        current_sum += arr[i]
        
        if current_sum - k in prefix_sum:
            max_length = max(max_length, i - prefix_sum[current_sum - k])
        
        if current_sum not in prefix_sum:
            prefix_sum[current_sum] = i
    
    return max_length

def longest_subarray_sum_k_with_count(arr, k):
    prefix_sum = {0: -1}
    max_length = 0
    current_sum = 0
    count = 0
    
    for i in range(len(arr)):
        current_sum += arr[i]
        
        if current_sum - k in prefix_sum:
            length = i - prefix_sum[current_sum - k]
            if length > max_length:
                max_length = length
                count = 1
            elif length == max_length:
                count += 1
        
        if current_sum not in prefix_sum:
            prefix_sum[current_sum] = i
    
    return max_length, count

def longest_subarray_sum_k_with_subarrays(arr, k):
    prefix_sum = {0: -1}
    max_length = 0
    current_sum = 0
    subarrays = []
    
    for i in range(len(arr)):
        current_sum += arr[i]
        
        if current_sum - k in prefix_sum:
            length = i - prefix_sum[current_sum - k]
            if length > max_length:
                max_length = length
                subarrays = [arr[prefix_sum[current_sum - k] + 1:i + 1]]
            elif length == max_length:
                subarrays.append(arr[prefix_sum[current_sum - k] + 1:i + 1])
        
        if current_sum not in prefix_sum:
            prefix_sum[current_sum] = i
    
    return max_length, subarrays

def longest_subarray_sum_k_with_negative(arr, k):
    prefix_sum = {0: -1}
    max_length = 0
    current_sum = 0
    
    for i in range(len(arr)):
        current_sum += arr[i]
        
        if current_sum - k in prefix_sum:
            max_length = max(max_length, i - prefix_sum[current_sum - k])
        
        if current_sum not in prefix_sum:
            prefix_sum[current_sum] = i
    
    return max_length

def longest_subarray_sum_k_with_circular(arr, k):
    n = len(arr)
    prefix_sum = {0: -1}
    max_length = 0
    current_sum = 0
    
    for i in range(2 * n):
        current_sum += arr[i % n]
        
        if current_sum - k in prefix_sum:
            max_length = max(max_length, i - prefix_sum[current_sum - k])
        
        if current_sum not in prefix_sum:
            prefix_sum[current_sum] = i
    
    return max_length

def longest_subarray_sum_k_with_validation_enhanced(arr, k):
    if not arr:
        return 0
    
    if k == 0:
        return 0
    
    prefix_sum = {0: -1}
    max_length = 0
    current_sum = 0
    
    for i in range(len(arr)):
        current_sum += arr[i]
        
        if current_sum - k in prefix_sum:
            max_length = max(max_length, i - prefix_sum[current_sum - k])
        
        if current_sum not in prefix_sum:
            prefix_sum[current_sum] = i
    
    return max_length

def longest_subarray_sum_k_with_optimization_enhanced(arr, k):
    prefix_sum = {0: -1}
    max_length = 0
    current_sum = 0
    
    for i in range(len(arr)):
        current_sum += arr[i]
        
        if current_sum - k in prefix_sum:
            max_length = max(max_length, i - prefix_sum[current_sum - k])
        
        if current_sum not in prefix_sum:
            prefix_sum[current_sum] = i
    
    return max_length

def longest_subarray_sum_k_with_advanced_optimization_enhanced(arr, k):
    prefix_sum = {0: -1}
    max_length = 0
    current_sum = 0
    
    for i in range(len(arr)):
        current_sum += arr[i]
        
        if current_sum - k in prefix_sum:
            max_length = max(max_length, i - prefix_sum[current_sum - k])
        
        if current_sum not in prefix_sum:
            prefix_sum[current_sum] = i
    
    return max_length

arr = [1, -1, 5, -2, 3]
k = 3

length1 = longest_subarray_sum_k_brute_force(arr, k)
length2 = longest_subarray_sum_k_hashmap(arr, k)
length3 = longest_subarray_sum_k_optimized(arr, k)
length4 = longest_subarray_sum_k_with_validation(arr, k)
length5 = longest_subarray_sum_k_with_optimization(arr, k)
length6 = longest_subarray_sum_k_with_advanced_optimization(arr, k)
length7, count = longest_subarray_sum_k_with_count(arr, k)
length8, subarrays = longest_subarray_sum_k_with_subarrays(arr, k)
length9 = longest_subarray_sum_k_with_negative(arr, k)
length10 = longest_subarray_sum_k_with_circular(arr, k)
length11 = longest_subarray_sum_k_with_validation_enhanced(arr, k)
length12 = longest_subarray_sum_k_with_optimization_enhanced(arr, k)
length13 = longest_subarray_sum_k_with_advanced_optimization_enhanced(arr, k)

print(f"Array: {arr}")
print(f"K: {k}")
print(f"Longest subarray (brute force): {length1}")
print(f"Longest subarray (hashmap): {length2}")
print(f"Longest subarray (optimized): {length3}")
print(f"Longest subarray (with validation): {length4}")
print(f"Longest subarray (with optimization): {length5}")
print(f"Longest subarray (advanced optimization): {length6}")
print(f"Longest subarray (with count): {length7}, Count: {count}")
print(f"Longest subarray (with subarrays): {length8}, Subarrays: {subarrays}")
print(f"Longest subarray (with negative): {length9}")
print(f"Longest subarray (with circular): {length10}")
print(f"Longest subarray (validation enhanced): {length11}")
print(f"Longest subarray (optimization enhanced): {length12}")
print(f"Longest subarray (advanced optimization enhanced): {length13}")
