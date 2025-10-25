def kadane_algorithm_basic(arr):
    max_so_far = arr[0]
    max_ending_here = arr[0]
    
    for i in range(1, len(arr)):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far

def kadane_algorithm_with_indices(arr):
    max_so_far = arr[0]
    max_ending_here = arr[0]
    start = 0
    end = 0
    temp_start = 0
    
    for i in range(1, len(arr)):
        if max_ending_here < 0:
            max_ending_here = arr[i]
            temp_start = i
        else:
            max_ending_here += arr[i]
        
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start = temp_start
            end = i
    
    return max_so_far, start, end

def kadane_algorithm_with_subarray(arr):
    max_so_far = arr[0]
    max_ending_here = arr[0]
    start = 0
    end = 0
    temp_start = 0
    
    for i in range(1, len(arr)):
        if max_ending_here < 0:
            max_ending_here = arr[i]
            temp_start = i
        else:
            max_ending_here += arr[i]
        
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start = temp_start
            end = i
    
    return max_so_far, arr[start:end+1]

def kadane_algorithm_with_validation(arr):
    if not arr:
        return 0
    
    if len(arr) == 1:
        return arr[0]
    
    max_so_far = arr[0]
    max_ending_here = arr[0]
    
    for i in range(1, len(arr)):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far

def kadane_algorithm_with_constraints(arr, constraints):
    max_so_far = arr[0]
    max_ending_here = arr[0]
    
    for i in range(1, len(arr)):
        if constraints(arr[i]):
            max_ending_here = max(arr[i], max_ending_here + arr[i])
            max_so_far = max(max_so_far, max_ending_here)
        else:
            max_ending_here = 0
    
    return max_so_far

def kadane_algorithm_with_optimization(arr):
    max_so_far = arr[0]
    max_ending_here = arr[0]
    
    for i in range(1, len(arr)):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far

def kadane_algorithm_with_advanced_optimization(arr):
    max_so_far = arr[0]
    max_ending_here = arr[0]
    
    for i in range(1, len(arr)):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far

def kadane_algorithm_with_count(arr):
    max_so_far = arr[0]
    max_ending_here = arr[0]
    count = 1
    
    for i in range(1, len(arr)):
        if max_ending_here + arr[i] > arr[i]:
            max_ending_here += arr[i]
        else:
            max_ending_here = arr[i]
            count = 1
        
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            count = 1
        elif max_ending_here == max_so_far:
            count += 1
    
    return max_so_far, count

def kadane_algorithm_with_negative_handling(arr):
    if all(x < 0 for x in arr):
        return max(arr)
    
    max_so_far = arr[0]
    max_ending_here = arr[0]
    
    for i in range(1, len(arr)):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far

def kadane_algorithm_with_circular_array(arr):
    def kadane(arr):
        max_so_far = arr[0]
        max_ending_here = arr[0]
        
        for i in range(1, len(arr)):
            max_ending_here = max(arr[i], max_ending_here + arr[i])
            max_so_far = max(max_so_far, max_ending_here)
        
        return max_so_far
    
    max_kadane = kadane(arr)
    max_wrap = sum(arr) - kadane([-x for x in arr])
    
    return max(max_kadane, max_wrap)

def kadane_algorithm_with_2d_array(matrix):
    def kadane_1d(arr):
        max_so_far = arr[0]
        max_ending_here = arr[0]
        
        for i in range(1, len(arr)):
            max_ending_here = max(arr[i], max_ending_here + arr[i])
            max_so_far = max(max_so_far, max_ending_here)
        
        return max_so_far
    
    max_sum = float('-inf')
    
    for left in range(len(matrix[0])):
        temp = [0] * len(matrix)
        
        for right in range(left, len(matrix[0])):
            for i in range(len(matrix)):
                temp[i] += matrix[i][right]
            
            current_sum = kadane_1d(temp)
            max_sum = max(max_sum, current_sum)
    
    return max_sum

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

kadane1 = kadane_algorithm_basic(arr)
kadane2, start, end = kadane_algorithm_with_indices(arr)
kadane3, subarray = kadane_algorithm_with_subarray(arr)
kadane4 = kadane_algorithm_with_validation(arr)
kadane5 = kadane_algorithm_with_optimization(arr)
kadane6 = kadane_algorithm_with_advanced_optimization(arr)
kadane7, count = kadane_algorithm_with_count(arr)
kadane8 = kadane_algorithm_with_negative_handling(arr)
kadane9 = kadane_algorithm_with_circular_array(arr)

matrix = [
    [1, 2, -1, -4, -20],
    [-8, -3, 4, 2, 1],
    [3, 8, 10, 1, 3],
    [-4, -1, 1, 7, -6]
]

kadane10 = kadane_algorithm_with_2d_array(matrix)

print(f"Array: {arr}")
print(f"Kadane (basic): {kadane1}")
print(f"Kadane (with indices): {kadane2}, Start: {start}, End: {end}")
print(f"Kadane (with subarray): {kadane3}, Subarray: {subarray}")
print(f"Kadane (with validation): {kadane4}")
print(f"Kadane (with optimization): {kadane5}")
print(f"Kadane (advanced optimization): {kadane6}")
print(f"Kadane (with count): {kadane7}, Count: {count}")
print(f"Kadane (negative handling): {kadane8}")
print(f"Kadane (circular array): {kadane9}")
print(f"Kadane (2D array): {kadane10}")
