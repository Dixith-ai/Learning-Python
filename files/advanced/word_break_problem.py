def word_break_recursive(s, word_dict):
    def helper(s):
        if not s:
            return True
        
        for i in range(1, len(s) + 1):
            if s[:i] in word_dict and helper(s[i:]):
                return True
        
        return False
    
    return helper(s)

def word_break_memoization(s, word_dict):
    memo = {}
    
    def helper(s):
        if s in memo:
            return memo[s]
        
        if not s:
            return True
        
        for i in range(1, len(s) + 1):
            if s[:i] in word_dict and helper(s[i:]):
                memo[s] = True
                return True
        
        memo[s] = False
        return False
    
    return helper(s)

def word_break_dp(s, word_dict):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break
    
    return dp[n]

def word_break_with_sentences(s, word_dict):
    def helper(s):
        if not s:
            return [[]]
        
        result = []
        for i in range(1, len(s) + 1):
            if s[:i] in word_dict:
                for sentence in helper(s[i:]):
                    result.append([s[:i]] + sentence)
        
        return result
    
    sentences = helper(s)
    return [sentence for sentence in sentences if sentence]

def word_break_with_optimization(s, word_dict):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break
    
    return dp[n]

def word_break_with_validation(s, word_dict):
    if not s:
        return True
    
    if not word_dict:
        return False
    
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break
    
    return dp[n]

def word_break_with_constraints(s, word_dict, constraints):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                if constraints(s[j:i]):
                    dp[i] = True
                    break
    
    return dp[n]

def word_break_with_count(s, word_dict):
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] > 0 and s[j:i] in word_dict:
                dp[i] += dp[j]
    
    return dp[n]

def word_break_with_optimization(s, word_dict):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break
    
    return dp[n]

def word_break_with_advanced_optimization(s, word_dict):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break
    
    return dp[n]

def word_break_with_trie(s, word_dict):
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.is_end = False
    
    def build_trie(words):
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end = True
        return root
    
    trie = build_trie(word_dict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break
    
    return dp[n]

s = "leetcode"
word_dict = {"leet", "code", "lee", "t"}

word_break1 = word_break_recursive(s, word_dict)
word_break2 = word_break_memoization(s, word_dict)
word_break3 = word_break_dp(s, word_dict)
word_break4 = word_break_with_sentences(s, word_dict)
word_break5 = word_break_with_optimization(s, word_dict)
word_break6 = word_break_with_validation(s, word_dict)
word_break7 = word_break_with_count(s, word_dict)
word_break8 = word_break_with_optimization(s, word_dict)
word_break9 = word_break_with_advanced_optimization(s, word_dict)
word_break10 = word_break_with_trie(s, word_dict)

print(f"String: {s}")
print(f"Word dict: {word_dict}")
print(f"Word break (recursive): {word_break1}")
print(f"Word break (memoization): {word_break2}")
print(f"Word break (DP): {word_break3}")
print(f"Word break (with sentences): {word_break4}")
print(f"Word break (with optimization): {word_break5}")
print(f"Word break (with validation): {word_break6}")
print(f"Word break (with count): {word_break7}")
print(f"Word break (with optimization): {word_break8}")
print(f"Word break (advanced optimization): {word_break9}")
print(f"Word break (with trie): {word_break10}")
