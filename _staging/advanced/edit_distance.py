def edit_distance_recursive(str1, str2):
    def helper(i, j):
        if i == 0:
            return j
        if j == 0:
            return i
        
        if str1[i - 1] == str2[j - 1]:
            return helper(i - 1, j - 1)
        else:
            return 1 + min(helper(i - 1, j), helper(i, j - 1), helper(i - 1, j - 1))
    
    return helper(len(str1), len(str2))

def edit_distance_memoization(str1, str2):
    memo = {}
    
    def helper(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i == 0:
            return j
        if j == 0:
            return i
        
        if str1[i - 1] == str2[j - 1]:
            memo[(i, j)] = helper(i - 1, j - 1)
        else:
            memo[(i, j)] = 1 + min(helper(i - 1, j), helper(i, j - 1), helper(i - 1, j - 1))
        
        return memo[(i, j)]
    
    return helper(len(str1), len(str2))

def edit_distance_dp(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    
    return dp[m][n]

def edit_distance_dp_optimized(str1, str2):
    if len(str1) < len(str2):
        str1, str2 = str2, str1
    
    m, n = len(str1), len(str2)
    prev = list(range(n + 1))
    curr = [0] * (n + 1)
    
    for i in range(1, m + 1):
        curr[0] = i
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                curr[j] = prev[j - 1]
            else:
                curr[j] = 1 + min(prev[j], curr[j - 1], prev[j - 1])
        prev, curr = curr, prev
    
    return prev[n]

def edit_distance_with_operations(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    
    operations = []
    i, j = m, n
    
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            i -= 1
            j -= 1
        else:
            if dp[i][j] == dp[i - 1][j] + 1:
                operations.append(f"Delete {str1[i - 1]}")
                i -= 1
            elif dp[i][j] == dp[i][j - 1] + 1:
                operations.append(f"Insert {str2[j - 1]}")
                j -= 1
            else:
                operations.append(f"Replace {str1[i - 1]} with {str2[j - 1]}")
                i -= 1
                j -= 1
    
    while i > 0:
        operations.append(f"Delete {str1[i - 1]}")
        i -= 1
    
    while j > 0:
        operations.append(f"Insert {str2[j - 1]}")
        j -= 1
    
    return dp[m][n], operations[::-1]

def edit_distance_with_weights(str1, str2, weights):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i * weights['delete']
    
    for j in range(n + 1):
        dp[0][j] = j * weights['insert']
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + weights['delete'],
                    dp[i][j - 1] + weights['insert'],
                    dp[i - 1][j - 1] + weights['replace']
                )
    
    return dp[m][n]

def edit_distance_with_constraints(str1, str2, constraints):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                if constraints(str1[i - 1], str2[j - 1]):
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                else:
                    dp[i][j] = float('inf')
    
    return dp[m][n]

def edit_distance_with_validation(str1, str2):
    if not str1 and not str2:
        return 0
    
    if not str1:
        return len(str2)
    
    if not str2:
        return len(str1)
    
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    
    return dp[m][n]

def edit_distance_with_optimization(str1, str2):
    if len(str1) < len(str2):
        str1, str2 = str2, str1
    
    m, n = len(str1), len(str2)
    prev = list(range(n + 1))
    curr = [0] * (n + 1)
    
    for i in range(1, m + 1):
        curr[0] = i
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                curr[j] = prev[j - 1]
            else:
                curr[j] = 1 + min(prev[j], curr[j - 1], prev[j - 1])
        prev, curr = curr, prev
    
    return prev[n]

def edit_distance_with_advanced_optimization(str1, str2):
    if len(str1) < len(str2):
        str1, str2 = str2, str1
    
    m, n = len(str1), len(str2)
    prev = list(range(n + 1))
    curr = [0] * (n + 1)
    
    for i in range(1, m + 1):
        curr[0] = i
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                curr[j] = prev[j - 1]
            else:
                curr[j] = 1 + min(prev[j], curr[j - 1], prev[j - 1])
        prev, curr = curr, prev
    
    return prev[n]

str1 = "kitten"
str2 = "sitting"
weights = {'delete': 1, 'insert': 1, 'replace': 1}

distance1 = edit_distance_recursive(str1, str2)
distance2 = edit_distance_memoization(str1, str2)
distance3 = edit_distance_dp(str1, str2)
distance4 = edit_distance_dp_optimized(str1, str2)
distance5, operations = edit_distance_with_operations(str1, str2)
distance6 = edit_distance_with_weights(str1, str2, weights)
distance7 = edit_distance_with_validation(str1, str2)
distance8 = edit_distance_with_optimization(str1, str2)
distance9 = edit_distance_with_advanced_optimization(str1, str2)

print(f"String 1: {str1}")
print(f"String 2: {str2}")
print(f"Edit distance (recursive): {distance1}")
print(f"Edit distance (memoization): {distance2}")
print(f"Edit distance (DP): {distance3}")
print(f"Edit distance (optimized): {distance4}")
print(f"Edit distance (with operations): {distance5}, Operations: {operations}")
print(f"Edit distance (with weights): {distance6}")
print(f"Edit distance (with validation): {distance7}")
print(f"Edit distance (with optimization): {distance8}")
print(f"Edit distance (advanced optimization): {distance9}")
