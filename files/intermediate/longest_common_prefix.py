def longest_common_prefix_vertical(strs):
    if not strs:
        return ""
    
    if len(strs) == 1:
        return strs[0]
    
    prefix = ""
    min_length = min(len(s) for s in strs)
    
    for i in range(min_length):
        char = strs[0][i]
        for s in strs[1:]:
            if s[i] != char:
                return prefix
        prefix += char
    
    return prefix

def longest_common_prefix_horizontal(strs):
    if not strs:
        return ""
    
    if len(strs) == 1:
        return strs[0]
    
    prefix = strs[0]
    
    for i in range(1, len(strs)):
        while not strs[i].startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix

def longest_common_prefix_divide_conquer(strs):
    if not strs:
        return ""
    
    if len(strs) == 1:
        return strs[0]
    
    def lcp_two_strings(s1, s2):
        min_length = min(len(s1), len(s2))
        for i in range(min_length):
            if s1[i] != s2[i]:
                return s1[:i]
        return s1[:min_length]
    
    def divide_conquer(left, right):
        if left == right:
            return strs[left]
        
        mid = (left + right) // 2
        left_lcp = divide_conquer(left, mid)
        right_lcp = divide_conquer(mid + 1, right)
        
        return lcp_two_strings(left_lcp, right_lcp)
    
    return divide_conquer(0, len(strs) - 1)

def longest_common_prefix_binary_search(strs):
    if not strs:
        return ""
    
    if len(strs) == 1:
        return strs[0]
    
    min_length = min(len(s) for s in strs)
    left, right = 0, min_length
    
    while left < right:
        mid = (left + right + 1) // 2
        prefix = strs[0][:mid]
        
        if all(s.startswith(prefix) for s in strs):
            left = mid
        else:
            right = mid - 1
    
    return strs[0][:left]

def longest_common_prefix_trie(strs):
    if not strs:
        return ""
    
    if len(strs) == 1:
        return strs[0]
    
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.is_end = False
            self.count = 0
    
    class Trie:
        def __init__(self):
            self.root = TrieNode()
        
        def insert(self, word):
            node = self.root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
                node.count += 1
            node.is_end = True
        
        def get_common_prefix(self, total_strings):
            node = self.root
            prefix = ""
            
            while len(node.children) == 1 and node.count == total_strings:
                char = list(node.children.keys())[0]
                prefix += char
                node = node.children[char]
            
            return prefix
    
    trie = Trie()
    for s in strs:
        trie.insert(s)
    
    return trie.get_common_prefix(len(strs))

def longest_common_prefix_optimized(strs):
    if not strs:
        return ""
    
    if len(strs) == 1:
        return strs[0]
    
    prefix = strs[0]
    
    for s in strs[1:]:
        i = 0
        while i < len(prefix) and i < len(s) and prefix[i] == s[i]:
            i += 1
        prefix = prefix[:i]
        
        if not prefix:
            break
    
    return prefix

def longest_common_prefix_recursive(strs):
    if not strs:
        return ""
    
    if len(strs) == 1:
        return strs[0]
    
    def lcp_two(s1, s2):
        if not s1 or not s2:
            return ""
        
        if s1[0] == s2[0]:
            return s1[0] + lcp_two(s1[1:], s2[1:])
        else:
            return ""
    
    def lcp_list(strings):
        if len(strings) == 1:
            return strings[0]
        
        mid = len(strings) // 2
        left_lcp = lcp_list(strings[:mid])
        right_lcp = lcp_list(strings[mid:])
        
        return lcp_two(left_lcp, right_lcp)
    
    return lcp_list(strs)

def longest_common_prefix_with_validation(strs):
    if not strs:
        return ""
    
    if len(strs) == 1:
        return strs[0]
    
    if any(not s for s in strs):
        return ""
    
    prefix = strs[0]
    
    for s in strs[1:]:
        if not s:
            return ""
        
        i = 0
        while i < len(prefix) and i < len(s) and prefix[i] == s[i]:
            i += 1
        
        prefix = prefix[:i]
        
        if not prefix:
            return ""
    
    return prefix

test_cases = [
    ["flower", "flow", "flight"],
    ["dog", "racecar", "car"],
    ["interspecies", "interstellar", "interstate"],
    ["throne", "throne"],
    ["", "b"],
    ["a", "ab"]
]

for strs in test_cases:
    lcp1 = longest_common_prefix_vertical(strs)
    lcp2 = longest_common_prefix_horizontal(strs)
    lcp3 = longest_common_prefix_divide_conquer(strs)
    lcp4 = longest_common_prefix_binary_search(strs)
    lcp5 = longest_common_prefix_trie(strs)
    lcp6 = longest_common_prefix_optimized(strs)
    lcp7 = longest_common_prefix_recursive(strs)
    lcp8 = longest_common_prefix_with_validation(strs)
    
    print(f"Strings: {strs}")
    print(f"LCP (vertical): '{lcp1}'")
    print(f"LCP (horizontal): '{lcp2}'")
    print(f"LCP (divide conquer): '{lcp3}'")
    print(f"LCP (binary search): '{lcp4}'")
    print(f"LCP (trie): '{lcp5}'")
    print(f"LCP (optimized): '{lcp6}'")
    print(f"LCP (recursive): '{lcp7}'")
    print(f"LCP (validation): '{lcp8}'")
    print()
