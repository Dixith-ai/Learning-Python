def climb_stairs_recursive(n):
    if n <= 2:
        return n
    
    return climb_stairs_recursive(n - 1) + climb_stairs_recursive(n - 2)

def climb_stairs_memoization(n):
    memo = {}
    
    def helper(n):
        if n in memo:
            return memo[n]
        
        if n <= 2:
            return n
        
        memo[n] = helper(n - 1) + helper(n - 2)
        return memo[n]
    
    return helper(n)

def climb_stairs_dp(n):
    if n <= 2:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

def climb_stairs_optimized(n):
    if n <= 2:
        return n
    
    prev2 = 1
    prev1 = 2
    
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    return prev1

def climb_stairs_matrix(n):
    if n <= 2:
        return n
    
    def matrix_multiply(A, B):
        return [[A[0][0] * B[0][0] + A[0][1] * B[1][0],
                 A[0][0] * B[0][1] + A[0][1] * B[1][1]],
                [A[1][0] * B[0][0] + A[1][1] * B[1][0],
                 A[1][0] * B[0][1] + A[1][1] * B[1][1]]]
    
    def matrix_power(matrix, power):
        if power == 1:
            return matrix
        
        if power % 2 == 0:
            half = matrix_power(matrix, power // 2)
            return matrix_multiply(half, half)
        else:
            return matrix_multiply(matrix, matrix_power(matrix, power - 1))
    
    base_matrix = [[1, 1], [1, 0]]
    result_matrix = matrix_power(base_matrix, n)
    
    return result_matrix[0][0]

def climb_stairs_with_steps(n, steps):
    if n == 0:
        return 1
    if n < 0:
        return 0
    
    total = 0
    for step in steps:
        total += climb_stairs_with_steps(n - step, steps)
    
    return total

def climb_stairs_with_steps_dp(n, steps):
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        for step in steps:
            if i >= step:
                dp[i] += dp[i - step]
    
    return dp[n]

def climb_stairs_with_constraints(n, max_consecutive):
    if n <= 0:
        return 1
    if n == 1:
        return 1
    
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2, n + 1):
        for j in range(1, min(i, max_consecutive) + 1):
            dp[i] += dp[i - j]
    
    return dp[n]

def climb_stairs_with_obstacles(n, obstacles):
    if n <= 0:
        return 1
    if 0 in obstacles:
        return 0
    
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        if i not in obstacles:
            if i >= 1:
                dp[i] += dp[i - 1]
            if i >= 2:
                dp[i] += dp[i - 2]
    
    return dp[n]

n = 5
steps = [1, 2, 3]
obstacles = [2, 4]

ways1 = climb_stairs_recursive(n)
ways2 = climb_stairs_memoization(n)
ways3 = climb_stairs_dp(n)
ways4 = climb_stairs_optimized(n)
ways5 = climb_stairs_matrix(n)
ways6 = climb_stairs_with_steps(n, steps)
ways7 = climb_stairs_with_steps_dp(n, steps)
ways8 = climb_stairs_with_constraints(n, 2)
ways9 = climb_stairs_with_obstacles(n, obstacles)

print(f"Number of ways to climb {n} stairs:")
print(f"Recursive: {ways1}")
print(f"Memoization: {ways2}")
print(f"Dynamic Programming: {ways3}")
print(f"Optimized: {ways4}")
print(f"Matrix: {ways5}")
print(f"With steps {steps}: {ways6}")
print(f"With steps DP: {ways7}")
print(f"With constraints (max 2): {ways8}")
print(f"With obstacles {obstacles}: {ways9}")
