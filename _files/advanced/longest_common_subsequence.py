def lcs_recursive(text1, text2):
    def helper(i, j):
        if i == 0 or j == 0:
            return 0
        
        if text1[i - 1] == text2[j - 1]:
            return 1 + helper(i - 1, j - 1)
        else:
            return max(helper(i - 1, j), helper(i, j - 1))
    
    return helper(len(text1), len(text2))

def lcs_memoization(text1, text2):
    memo = {}
    
    def helper(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i == 0 or j == 0:
            return 0
        
        if text1[i - 1] == text2[j - 1]:
            memo[(i, j)] = 1 + helper(i - 1, j - 1)
        else:
            memo[(i, j)] = max(helper(i - 1, j), helper(i, j - 1))
        
        return memo[(i, j)]
    
    return helper(len(text1), len(text2))

def lcs_dp(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

def lcs_dp_optimized(text1, text2):
    if len(text1) < len(text2):
        text1, text2 = text2, text1
    
    m, n = len(text1), len(text2)
    prev = [0] * (n + 1)
    curr = [0] * (n + 1)
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                curr[j] = 1 + prev[j - 1]
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev, curr = curr, prev
    
    return prev[n]

def lcs_with_sequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    sequence = []
    i, j = m, n
    while i > 0 and j > 0:
        if text1[i - 1] == text2[j - 1]:
            sequence.append(text1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    return dp[m][n], sequence[::-1]

def lcs_with_all_sequences(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    def find_all_sequences(i, j):
        if i == 0 or j == 0:
            return [""]
        
        if text1[i - 1] == text2[j - 1]:
            sequences = find_all_sequences(i - 1, j - 1)
            return [seq + text1[i - 1] for seq in sequences]
        else:
            sequences = []
            if dp[i - 1][j] == dp[i][j]:
                sequences.extend(find_all_sequences(i - 1, j))
            if dp[i][j - 1] == dp[i][j]:
                sequences.extend(find_all_sequences(i, j - 1))
            return sequences
    
    return dp[m][n], find_all_sequences(m, n)

def lcs_with_length(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

def lcs_with_validation(text1, text2):
    if not text1 or not text2:
        return 0
    
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

def lcs_with_constraints(text1, text2, max_length):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = min(1 + dp[i - 1][j - 1], max_length)
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

text1 = "ABCDGH"
text2 = "AEDFHR"

lcs1 = lcs_recursive(text1, text2)
lcs2 = lcs_memoization(text1, text2)
lcs3 = lcs_dp(text1, text2)
lcs4 = lcs_dp_optimized(text1, text2)
lcs5, sequence = lcs_with_sequence(text1, text2)
lcs6, all_sequences = lcs_with_all_sequences(text1, text2)
lcs7 = lcs_with_length(text1, text2)
lcs8 = lcs_with_validation(text1, text2)
lcs9 = lcs_with_constraints(text1, text2, 3)

print(f"Text1: {text1}")
print(f"Text2: {text2}")
print(f"LCS (recursive): {lcs1}")
print(f"LCS (memoization): {lcs2}")
print(f"LCS (DP): {lcs3}")
print(f"LCS (optimized): {lcs4}")
print(f"LCS (with sequence): {lcs5}, Sequence: {sequence}")
print(f"LCS (with all sequences): {lcs6}, Sequences: {all_sequences}")
print(f"LCS (with length): {lcs7}")
print(f"LCS (with validation): {lcs8}")
print(f"LCS (with constraints): {lcs9}")
