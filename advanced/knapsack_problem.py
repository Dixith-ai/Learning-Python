def knapsack_recursive(weights, values, capacity):
    def helper(n, w):
        if n == 0 or w == 0:
            return 0
        
        if weights[n - 1] > w:
            return helper(n - 1, w)
        else:
            return max(values[n - 1] + helper(n - 1, w - weights[n - 1]),
                      helper(n - 1, w))
    
    return helper(len(weights), capacity)

def knapsack_memoization(weights, values, capacity):
    memo = {}
    
    def helper(n, w):
        if (n, w) in memo:
            return memo[(n, w)]
        
        if n == 0 or w == 0:
            return 0
        
        if weights[n - 1] > w:
            memo[(n, w)] = helper(n - 1, w)
        else:
            memo[(n, w)] = max(values[n - 1] + helper(n - 1, w - weights[n - 1]),
                              helper(n - 1, w))
        
        return memo[(n, w)]
    
    return helper(len(weights), capacity)

def knapsack_dp(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]],
                              dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]

def knapsack_dp_optimized(weights, values, capacity):
    dp = [0] * (capacity + 1)
    
    for i in range(len(weights)):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])
    
    return dp[capacity]

def knapsack_with_items(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]],
                              dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    
    items = []
    i, w = n, capacity
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            items.append(i - 1)
            w -= weights[i - 1]
        i -= 1
    
    return dp[n][capacity], items[::-1]

def knapsack_fractional(weights, values, capacity):
    items = list(zip(values, weights))
    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    
    total_value = 0
    remaining_capacity = capacity
    
    for value, weight in items:
        if remaining_capacity >= weight:
            total_value += value
            remaining_capacity -= weight
        else:
            total_value += value * (remaining_capacity / weight)
            break
    
    return total_value

def knapsack_multiple_items(weights, values, capacity, quantities):
    n = len(weights)
    dp = [0] * (capacity + 1)
    
    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            for k in range(1, min(quantities[i], w // weights[i]) + 1):
                dp[w] = max(dp[w], k * values[i] + dp[w - k * weights[i]])
    
    return dp[capacity]

def knapsack_with_constraints(weights, values, capacity, max_items):
    n = len(weights)
    dp = [[[0] * (max_items + 1) for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            for k in range(1, max_items + 1):
                if weights[i - 1] <= w:
                    dp[i][w][k] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]][k - 1],
                                     dp[i - 1][w][k])
                else:
                    dp[i][w][k] = dp[i - 1][w][k]
    
    return dp[n][capacity][max_items]

def knapsack_with_validation(weights, values, capacity):
    if not weights or not values or len(weights) != len(values):
        return 0
    
    if capacity <= 0:
        return 0
    
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]],
                              dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]

def knapsack_with_optimization(weights, values, capacity):
    if not weights or not values:
        return 0
    
    n = len(weights)
    dp = [0] * (capacity + 1)
    
    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])
    
    return dp[capacity]

weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
quantities = [1, 1, 1]
max_items = 2

knapsack1 = knapsack_recursive(weights, values, capacity)
knapsack2 = knapsack_memoization(weights, values, capacity)
knapsack3 = knapsack_dp(weights, values, capacity)
knapsack4 = knapsack_dp_optimized(weights, values, capacity)
knapsack5, items = knapsack_with_items(weights, values, capacity)
knapsack6 = knapsack_fractional(weights, values, capacity)
knapsack7 = knapsack_multiple_items(weights, values, capacity, quantities)
knapsack8 = knapsack_with_constraints(weights, values, capacity, max_items)
knapsack9 = knapsack_with_validation(weights, values, capacity)
knapsack10 = knapsack_with_optimization(weights, values, capacity)

print(f"Weights: {weights}")
print(f"Values: {values}")
print(f"Capacity: {capacity}")
print(f"Knapsack (recursive): {knapsack1}")
print(f"Knapsack (memoization): {knapsack2}")
print(f"Knapsack (DP): {knapsack3}")
print(f"Knapsack (optimized): {knapsack4}")
print(f"Knapsack (with items): {knapsack5}, Items: {items}")
print(f"Knapsack (fractional): {knapsack6}")
print(f"Knapsack (multiple items): {knapsack7}")
print(f"Knapsack (with constraints): {knapsack8}")
print(f"Knapsack (with validation): {knapsack9}")
print(f"Knapsack (with optimization): {knapsack10}")
