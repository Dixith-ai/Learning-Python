def coin_change_recursive(coins, amount):
    def helper(amount):
        if amount == 0:
            return 0
        if amount < 0:
            return float('inf')
        
        min_coins = float('inf')
        for coin in coins:
            result = helper(amount - coin)
            if result != float('inf'):
                min_coins = min(min_coins, 1 + result)
        
        return min_coins
    
    result = helper(amount)
    return result if result != float('inf') else -1

def coin_change_memoization(coins, amount):
    memo = {}
    
    def helper(amount):
        if amount in memo:
            return memo[amount]
        
        if amount == 0:
            return 0
        if amount < 0:
            return float('inf')
        
        min_coins = float('inf')
        for coin in coins:
            result = helper(amount - coin)
            if result != float('inf'):
                min_coins = min(min_coins, 1 + result)
        
        memo[amount] = min_coins
        return min_coins
    
    result = helper(amount)
    return result if result != float('inf') else -1

def coin_change_dp(coins, amount):
    if amount == 0:
        return 0
    
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], 1 + dp[i - coin])
    
    return dp[amount] if dp[amount] != float('inf') else -1

def coin_change_with_coins(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [-1] * (amount + 1)
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin
    
    if dp[amount] == float('inf'):
        return -1, []
    
    coins_used = []
    remaining = amount
    while remaining > 0:
        coin = coin_used[remaining]
        coins_used.append(coin)
        remaining -= coin
    
    return dp[amount], coins_used

def coin_change_ways(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    
    return dp[amount]

def coin_change_ways_with_validation(coins, amount):
    if amount == 0:
        return 1
    
    if not coins:
        return 0
    
    dp = [0] * (amount + 1)
    dp[0] = 1
    
    for coin in coins:
        if coin > 0:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
    
    return dp[amount]

def coin_change_with_constraints(coins, amount, max_coins):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 <= max_coins:
                dp[i] = min(dp[i], 1 + dp[i - coin])
    
    return dp[amount] if dp[amount] != float('inf') else -1

def coin_change_with_optimization(coins, amount):
    if amount == 0:
        return 0
    
    coins.sort(reverse=True)
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], 1 + dp[i - coin])
    
    return dp[amount] if dp[amount] != float('inf') else -1

def coin_change_with_validation_enhanced(coins, amount):
    if amount == 0:
        return 0
    
    if not coins:
        return -1
    
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin > 0 and coin <= i:
                dp[i] = min(dp[i], 1 + dp[i - coin])
    
    return dp[amount] if dp[amount] != float('inf') else -1

def coin_change_with_levels(coins, amount):
    if amount == 0:
        return 0
    
    level = 0
    queue = [amount]
    visited = set()
    
    while queue:
        level += 1
        next_level = []
        
        for remaining in queue:
            if remaining in visited:
                continue
            visited.add(remaining)
            
            for coin in coins:
                if coin == remaining:
                    return level
                if coin < remaining:
                    next_level.append(remaining - coin)
        
        queue = next_level
    
    return -1

def coin_change_with_bfs(coins, amount):
    if amount == 0:
        return 0
    
    queue = [(amount, 0)]
    visited = set()
    
    while queue:
        remaining, steps = queue.pop(0)
        
        if remaining == 0:
            return steps
        
        if remaining in visited:
            continue
        visited.add(remaining)
        
        for coin in coins:
            if coin <= remaining:
                queue.append((remaining - coin, steps + 1))
    
    return -1

coins = [1, 3, 4]
amount = 6

change1 = coin_change_recursive(coins, amount)
change2 = coin_change_memoization(coins, amount)
change3 = coin_change_dp(coins, amount)
change4, coins_used = coin_change_with_coins(coins, amount)
change5 = coin_change_ways(coins, amount)
change6 = coin_change_ways_with_validation(coins, amount)
change7 = coin_change_with_constraints(coins, amount, 3)
change8 = coin_change_with_optimization(coins, amount)
change9 = coin_change_with_validation_enhanced(coins, amount)
change10 = coin_change_with_levels(coins, amount)
change11 = coin_change_with_bfs(coins, amount)

print(f"Coins: {coins}")
print(f"Amount: {amount}")
print(f"Coin change (recursive): {change1}")
print(f"Coin change (memoization): {change2}")
print(f"Coin change (DP): {change3}")
print(f"Coin change (with coins): {change4}, Coins used: {coins_used}")
print(f"Coin change ways: {change5}")
print(f"Coin change ways (validation): {change6}")
print(f"Coin change (with constraints): {change7}")
print(f"Coin change (optimization): {change8}")
print(f"Coin change (validation enhanced): {change9}")
print(f"Coin change (levels): {change10}")
print(f"Coin change (BFS): {change11}")
