def max_sum_subarray_k(arr, k):
    if not arr or k <= 0 or k > len(arr):
        return 0
    
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

def max_sum_subarray_k_optimized(arr, k):
    if not arr or k <= 0 or k > len(arr):
        return 0
    
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

def max_sum_subarray_k_with_indices(arr, k):
    if not arr or k <= 0 or k > len(arr):
        return 0, -1, -1
    
    window_sum = sum(arr[:k])
    max_sum = window_sum
    start = 0
    end = k - 1
    
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        if window_sum > max_sum:
            max_sum = window_sum
            start = i - k + 1
            end = i
    
    return max_sum, start, end

def max_sum_subarray_k_with_validation(arr, k):
    if not arr or k <= 0 or k > len(arr):
        return 0
    
    if k == 1:
        return max(arr)
    
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

def max_sum_subarray_k_with_constraints(arr, k, constraints):
    if not arr or k <= 0 or k > len(arr):
        return 0
    
    window_sum = sum(arr[:k])
    max_sum = window_sum if constraints(arr[:k]) else 0
    
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        if constraints(arr[i - k + 1:i + 1]):
            max_sum = max(max_sum, window_sum)
    
    return max_sum

def max_sum_subarray_k_with_optimization(arr, k):
    if not arr or k <= 0 or k > len(arr):
        return 0
    
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

def max_sum_subarray_k_with_advanced_optimization(arr, k):
    if not arr or k <= 0 or k > len(arr):
        return 0
    
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

def max_sum_subarray_k_with_count(arr, k):
    if not arr or k <= 0 or k > len(arr):
        return 0, 0
    
    window_sum = sum(arr[:k])
    max_sum = window_sum
    count = 1
    
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        if window_sum > max_sum:
            max_sum = window_sum
            count = 1
        elif window_sum == max_sum:
            count += 1
    
    return max_sum, count

def max_sum_subarray_k_with_subarrays(arr, k):
    if not arr or k <= 0 or k > len(arr):
        return 0, []
    
    window_sum = sum(arr[:k])
    max_sum = window_sum
    max_subarrays = [arr[:k]]
    
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        if window_sum > max_sum:
            max_sum = window_sum
            max_subarrays = [arr[i - k + 1:i + 1]]
        elif window_sum == max_sum:
            max_subarrays.append(arr[i - k + 1:i + 1])
    
    return max_sum, max_subarrays

def max_sum_subarray_k_with_negative(arr, k):
    if not arr or k <= 0 or k > len(arr):
        return 0
    
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

def max_sum_subarray_k_with_circular(arr, k):
    if not arr or k <= 0 or k > len(arr):
        return 0
    
    n = len(arr)
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, n + k):
        window_sum = window_sum - arr[(i - k) % n] + arr[i % n]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4

max_sum1 = max_sum_subarray_k(arr, k)
max_sum2 = max_sum_subarray_k_optimized(arr, k)
max_sum3, start, end = max_sum_subarray_k_with_indices(arr, k)
max_sum4 = max_sum_subarray_k_with_validation(arr, k)
max_sum5 = max_sum_subarray_k_with_optimization(arr, k)
max_sum6 = max_sum_subarray_k_with_advanced_optimization(arr, k)
max_sum7, count = max_sum_subarray_k_with_count(arr, k)
max_sum8, subarrays = max_sum_subarray_k_with_subarrays(arr, k)
max_sum9 = max_sum_subarray_k_with_negative(arr, k)
max_sum10 = max_sum_subarray_k_with_circular(arr, k)

print(f"Array: {arr}")
print(f"K: {k}")
print(f"Max sum (basic): {max_sum1}")
print(f"Max sum (optimized): {max_sum2}")
print(f"Max sum (with indices): {max_sum3}, Start: {start}, End: {end}")
print(f"Max sum (with validation): {max_sum4}")
print(f"Max sum (with optimization): {max_sum5}")
print(f"Max sum (advanced optimization): {max_sum6}")
print(f"Max sum (with count): {max_sum7}, Count: {count}")
print(f"Max sum (with subarrays): {max_sum8}, Subarrays: {subarrays}")
print(f"Max sum (with negative): {max_sum9}")
print(f"Max sum (with circular): {max_sum10}")
