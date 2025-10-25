def partition_problem_recursive(arr):
    def helper(index, sum1, sum2):
        if index == len(arr):
            return sum1 == sum2
        
        return (helper(index + 1, sum1 + arr[index], sum2) or
                helper(index + 1, sum1, sum2 + arr[index]))
    
    return helper(0, 0, 0)

def partition_problem_memoization(arr):
    memo = {}
    
    def helper(index, sum1, sum2):
        if (index, sum1, sum2) in memo:
            return memo[(index, sum1, sum2)]
        
        if index == len(arr):
            return sum1 == sum2
        
        result = (helper(index + 1, sum1 + arr[index], sum2) or
                 helper(index + 1, sum1, sum2 + arr[index]))
        
        memo[(index, sum1, sum2)] = result
        return result
    
    return helper(0, 0, 0)

def partition_problem_dp(arr):
    total_sum = sum(arr)
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    n = len(arr)
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = True
    
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if arr[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
    
    return dp[n][target]

def partition_problem_dp_optimized(arr):
    total_sum = sum(arr)
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    dp = [False] * (target + 1)
    dp[0] = True
    
    for num in arr:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    
    return dp[target]

def partition_problem_with_subsets(arr):
    total_sum = sum(arr)
    if total_sum % 2 != 0:
        return False, [], []
    
    target = total_sum // 2
    n = len(arr)
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = True
    
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if arr[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
    
    if not dp[n][target]:
        return False, [], []
    
    subset1 = []
    subset2 = []
    i, j = n, target
    
    while i > 0 and j > 0:
        if dp[i - 1][j]:
            subset2.append(arr[i - 1])
            i -= 1
        else:
            subset1.append(arr[i - 1])
            j -= arr[i - 1]
            i -= 1
    
    while i > 0:
        subset2.append(arr[i - 1])
        i -= 1
    
    return True, subset1, subset2

def partition_problem_with_validation(arr):
    if not arr:
        return True
    
    if len(arr) == 1:
        return False
    
    total_sum = sum(arr)
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    dp = [False] * (target + 1)
    dp[0] = True
    
    for num in arr:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    
    return dp[target]

def partition_problem_with_constraints(arr, constraints):
    total_sum = sum(arr)
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    dp = [False] * (target + 1)
    dp[0] = True
    
    for num in arr:
        if constraints(num):
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
    
    return dp[target]

def partition_problem_with_optimization(arr):
    total_sum = sum(arr)
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    dp = [False] * (target + 1)
    dp[0] = True
    
    for num in arr:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    
    return dp[target]

def partition_problem_with_advanced_optimization(arr):
    total_sum = sum(arr)
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    dp = [False] * (target + 1)
    dp[0] = True
    
    for num in arr:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    
    return dp[target]

def partition_problem_with_count(arr):
    total_sum = sum(arr)
    if total_sum % 2 != 0:
        return 0
    
    target = total_sum // 2
    dp = [0] * (target + 1)
    dp[0] = 1
    
    for num in arr:
        for j in range(target, num - 1, -1):
            dp[j] += dp[j - num]
    
    return dp[target]

arr = [1, 5, 11, 5]

partition1 = partition_problem_recursive(arr)
partition2 = partition_problem_memoization(arr)
partition3 = partition_problem_dp(arr)
partition4 = partition_problem_dp_optimized(arr)
partition5, subset1, subset2 = partition_problem_with_subsets(arr)
partition6 = partition_problem_with_validation(arr)
partition7 = partition_problem_with_optimization(arr)
partition8 = partition_problem_with_advanced_optimization(arr)
partition9 = partition_problem_with_count(arr)

print(f"Array: {arr}")
print(f"Partition (recursive): {partition1}")
print(f"Partition (memoization): {partition2}")
print(f"Partition (DP): {partition3}")
print(f"Partition (optimized): {partition4}")
print(f"Partition (with subsets): {partition5}, Subset1: {subset1}, Subset2: {subset2}")
print(f"Partition (with validation): {partition6}")
print(f"Partition (with optimization): {partition7}")
print(f"Partition (advanced optimization): {partition8}")
print(f"Partition (with count): {partition9}")
