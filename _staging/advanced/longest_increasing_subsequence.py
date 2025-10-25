def lis_recursive(arr):
    def helper(i, prev):
        if i == len(arr):
            return 0
        
        if arr[i] > prev:
            return max(1 + helper(i + 1, arr[i]), helper(i + 1, prev))
        else:
            return helper(i + 1, prev)
    
    return helper(0, float('-inf'))

def lis_memoization(arr):
    memo = {}
    
    def helper(i, prev):
        if (i, prev) in memo:
            return memo[(i, prev)]
        
        if i == len(arr):
            return 0
        
        if arr[i] > prev:
            memo[(i, prev)] = max(1 + helper(i + 1, arr[i]), helper(i + 1, prev))
        else:
            memo[(i, prev)] = helper(i + 1, prev)
        
        return memo[(i, prev)]
    
    return helper(0, float('-inf'))

def lis_dp(arr):
    if not arr:
        return 0
    
    n = len(arr)
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

def lis_dp_optimized(arr):
    if not arr:
        return 0
    
    tails = []
    
    for num in arr:
        left, right = 0, len(tails)
        while left < right:
            mid = (left + right) // 2
            if tails[mid] < num:
                left = mid + 1
            else:
                right = mid
        
        if left == len(tails):
            tails.append(num)
        else:
            tails[left] = num
    
    return len(tails)

def lis_with_sequence(arr):
    if not arr:
        return 0, []
    
    n = len(arr)
    dp = [1] * n
    parent = [-1] * n
    
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j
    
    max_length = max(dp)
    max_index = dp.index(max_length)
    
    sequence = []
    while max_index != -1:
        sequence.append(arr[max_index])
        max_index = parent[max_index]
    
    return max_length, sequence[::-1]

def lis_with_all_sequences(arr):
    if not arr:
        return 0, []
    
    n = len(arr)
    dp = [1] * n
    parent = [-1] * n
    
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j
    
    max_length = max(dp)
    
    def find_all_sequences(index, length):
        if length == 0:
            return [[]]
        
        sequences = []
        for i in range(index):
            if arr[i] < arr[index] and dp[i] == length - 1:
                for seq in find_all_sequences(i, length - 1):
                    sequences.append(seq + [arr[index]])
        
        return sequences
    
    all_sequences = []
    for i in range(n):
        if dp[i] == max_length:
            all_sequences.extend(find_all_sequences(i, max_length))
    
    return max_length, all_sequences

def lis_with_binary_search(arr):
    if not arr:
        return 0
    
    tails = []
    
    for num in arr:
        left, right = 0, len(tails)
        while left < right:
            mid = (left + right) // 2)
            if tails[mid] < num:
                left = mid + 1
            else:
                right = mid
        
        if left == len(tails):
            tails.append(num)
        else:
            tails[left] = num
    
    return len(tails)

def lis_with_validation(arr):
    if not arr:
        return 0
    
    if len(arr) == 1:
        return 1
    
    n = len(arr)
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

def lis_with_constraints(arr, max_length):
    if not arr:
        return 0
    
    n = len(arr)
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return min(max(dp), max_length)

def lis_with_optimization(arr):
    if not arr:
        return 0
    
    tails = []
    
    for num in arr:
        left, right = 0, len(tails)
        while left < right:
            mid = (left + right) // 2
            if tails[mid] < num:
                left = mid + 1
            else:
                right = mid
        
        if left == len(tails):
            tails.append(num)
        else:
            tails[left] = num
    
    return len(tails)

arr = [10, 9, 2, 5, 3, 7, 101, 18]

lis1 = lis_recursive(arr)
lis2 = lis_memoization(arr)
lis3 = lis_dp(arr)
lis4 = lis_dp_optimized(arr)
lis5, sequence = lis_with_sequence(arr)
lis6, all_sequences = lis_with_all_sequences(arr)
lis7 = lis_with_binary_search(arr)
lis8 = lis_with_validation(arr)
lis9 = lis_with_constraints(arr, 4)
lis10 = lis_with_optimization(arr)

print(f"Array: {arr}")
print(f"LIS (recursive): {lis1}")
print(f"LIS (memoization): {lis2}")
print(f"LIS (DP): {lis3}")
print(f"LIS (optimized): {lis4}")
print(f"LIS (with sequence): {lis5}, Sequence: {sequence}")
print(f"LIS (with all sequences): {lis6}, Sequences: {all_sequences}")
print(f"LIS (binary search): {lis7}")
print(f"LIS (with validation): {lis8}")
print(f"LIS (with constraints): {lis9}")
print(f"LIS (with optimization): {lis10}")
