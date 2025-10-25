def matrix_chain_multiplication_recursive(dimensions):
    def helper(i, j):
        if i == j:
            return 0
        
        min_cost = float('inf')
        for k in range(i, j):
            cost = (helper(i, k) + helper(k + 1, j) + 
                   dimensions[i] * dimensions[k + 1] * dimensions[j + 1])
            min_cost = min(min_cost, cost)
        
        return min_cost
    
    return helper(0, len(dimensions) - 2)

def matrix_chain_multiplication_memoization(dimensions):
    memo = {}
    
    def helper(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i == j:
            return 0
        
        min_cost = float('inf')
        for k in range(i, j):
            cost = (helper(i, k) + helper(k + 1, j) + 
                   dimensions[i] * dimensions[k + 1] * dimensions[j + 1])
            min_cost = min(min_cost, cost)
        
        memo[(i, j)] = min_cost
        return min_cost
    
    return helper(0, len(dimensions) - 2)

def matrix_chain_multiplication_dp(dimensions):
    n = len(dimensions) - 1
    dp = [[0] * n for _ in range(n)]
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            
            for k in range(i, j):
                cost = (dp[i][k] + dp[k + 1][j] + 
                       dimensions[i] * dimensions[k + 1] * dimensions[j + 1])
                dp[i][j] = min(dp[i][j], cost)
    
    return dp[0][n - 1]

def matrix_chain_multiplication_with_parentheses(dimensions):
    n = len(dimensions) - 1
    dp = [[0] * n for _ in range(n)]
    parent = [[0] * n for _ in range(n)]
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            
            for k in range(i, j):
                cost = (dp[i][k] + dp[k + 1][j] + 
                       dimensions[i] * dimensions[k + 1] * dimensions[j + 1])
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    parent[i][j] = k
    
    def get_parentheses(i, j):
        if i == j:
            return f"A{i}"
        else:
            k = parent[i][j]
            left = get_parentheses(i, k)
            right = get_parentheses(k + 1, j)
            return f"({left}{right})"
    
    return dp[0][n - 1], get_parentheses(0, n - 1)

def matrix_chain_multiplication_optimized(dimensions):
    n = len(dimensions) - 1
    dp = [[0] * n for _ in range(n)]
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            
            for k in range(i, j):
                cost = (dp[i][k] + dp[k + 1][j] + 
                       dimensions[i] * dimensions[k + 1] * dimensions[j + 1])
                dp[i][j] = min(dp[i][j], cost)
    
    return dp[0][n - 1]

def matrix_chain_multiplication_with_validation(dimensions):
    if not dimensions or len(dimensions) < 2:
        return 0
    
    n = len(dimensions) - 1
    dp = [[0] * n for _ in range(n)]
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            
            for k in range(i, j):
                cost = (dp[i][k] + dp[k + 1][j] + 
                       dimensions[i] * dimensions[k + 1] * dimensions[j + 1])
                dp[i][j] = min(dp[i][j], cost)
    
    return dp[0][n - 1]

def matrix_chain_multiplication_with_constraints(dimensions, constraints):
    n = len(dimensions) - 1
    dp = [[0] * n for _ in range(n)]
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            
            for k in range(i, j):
                if constraints(i, k, j):
                    cost = (dp[i][k] + dp[k + 1][j] + 
                           dimensions[i] * dimensions[k + 1] * dimensions[j + 1])
                    dp[i][j] = min(dp[i][j], cost)
    
    return dp[0][n - 1]

def matrix_chain_multiplication_with_optimization(dimensions):
    n = len(dimensions) - 1)
    dp = [[0] * n for _ in range(n)]
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            
            for k in range(i, j):
                cost = (dp[i][k] + dp[k + 1][j] + 
                       dimensions[i] * dimensions[k + 1] * dimensions[j + 1])
                dp[i][j] = min(dp[i][j], cost)
    
    return dp[0][n - 1]

def matrix_chain_multiplication_with_count(dimensions):
    n = len(dimensions) - 1
    dp = [[0] * n for _ in range(n)]
    count = [[0] * n for _ in range(n)]
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            
            for k in range(i, j):
                cost = (dp[i][k] + dp[k + 1][j] + 
                       dimensions[i] * dimensions[k + 1] * dimensions[j + 1])
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    count[i][j] = 1
                elif cost == dp[i][j]:
                    count[i][j] += 1
    
    return dp[0][n - 1], count[0][n - 1]

def matrix_chain_multiplication_with_advanced_optimization(dimensions):
    n = len(dimensions) - 1
    dp = [[0] * n for _ in range(n)]
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            
            for k in range(i, j):
                cost = (dp[i][k] + dp[k + 1][j] + 
                       dimensions[i] * dimensions[k + 1] * dimensions[j + 1])
                dp[i][j] = min(dp[i][j], cost)
    
    return dp[0][n - 1]

dimensions = [1, 2, 3, 4, 5]

mcm1 = matrix_chain_multiplication_recursive(dimensions)
mcm2 = matrix_chain_multiplication_memoization(dimensions)
mcm3 = matrix_chain_multiplication_dp(dimensions)
mcm4, parentheses = matrix_chain_multiplication_with_parentheses(dimensions)
mcm5 = matrix_chain_multiplication_optimized(dimensions)
mcm6 = matrix_chain_multiplication_with_validation(dimensions)
mcm7 = matrix_chain_multiplication_with_optimization(dimensions)
mcm8, count = matrix_chain_multiplication_with_count(dimensions)
mcm9 = matrix_chain_multiplication_with_advanced_optimization(dimensions)

print(f"Dimensions: {dimensions}")
print(f"Matrix chain multiplication (recursive): {mcm1}")
print(f"Matrix chain multiplication (memoization): {mcm2}")
print(f"Matrix chain multiplication (DP): {mcm3}")
print(f"Matrix chain multiplication (with parentheses): {mcm4}, Parentheses: {parentheses}")
print(f"Matrix chain multiplication (optimized): {mcm5}")
print(f"Matrix chain multiplication (with validation): {mcm6}")
print(f"Matrix chain multiplication (with optimization): {mcm7}")
print(f"Matrix chain multiplication (with count): {mcm8}, Count: {count}")
print(f"Matrix chain multiplication (advanced optimization): {mcm9}")
