def find_anagrams_brute_force(s, p):
    if len(p) > len(s):
        return []
    
    result = []
    p_sorted = sorted(p)
    
    for i in range(len(s) - len(p) + 1):
        substring = s[i:i + len(p)]
        if sorted(substring) == p_sorted:
            result.append(i)
    
    return result

def find_anagrams_sliding_window(s, p):
    if len(p) > len(s):
        return []
    
    from collections import Counter
    
    p_count = Counter(p)
    window_count = Counter()
    result = []
    
    for i in range(len(s)):
        window_count[s[i]] += 1
        
        if i >= len(p):
            left_char = s[i - len(p)]
            if window_count[left_char] == 1:
                del window_count[left_char]
            else:
                window_count[left_char] -= 1
        
        if window_count == p_count:
            result.append(i - len(p) + 1)
    
    return result

def find_anagrams_optimized(s, p):
    if len(p) > len(s):
        return []
    
    from collections import Counter
    
    p_count = Counter(p)
    window_count = Counter()
    result = []
    
    for i in range(len(s)):
        window_count[s[i]] += 1
        
        if i >= len(p):
            left_char = s[i - len(p)]
            if window_count[left_char] == 1:
                del window_count[left_char]
            else:
                window_count[left_char] -= 1
        
        if window_count == p_count:
            result.append(i - len(p) + 1)
    
    return result

def find_anagrams_with_validation(s, p):
    if not s or not p:
        return []
    
    if len(p) > len(s):
        return []
    
    from collections import Counter
    
    p_count = Counter(p)
    window_count = Counter()
    result = []
    
    for i in range(len(s)):
        window_count[s[i]] += 1
        
        if i >= len(p):
            left_char = s[i - len(p)]
            if window_count[left_char] == 1:
                del window_count[left_char]
            else:
                window_count[left_char] -= 1
        
        if window_count == p_count:
            result.append(i - len(p) + 1)
    
    return result

def find_anagrams_with_constraints(s, p, constraints):
    if len(p) > len(s):
        return []
    
    from collections import Counter
    
    p_count = Counter(p)
    window_count = Counter()
    result = []
    
    for i in range(len(s)):
        if constraints(s[i]):
            window_count[s[i]] += 1
            
            if i >= len(p):
                left_char = s[i - len(p)]
                if constraints(left_char):
                    if window_count[left_char] == 1:
                        del window_count[left_char]
                    else:
                        window_count[left_char] -= 1
            
            if window_count == p_count:
                result.append(i - len(p) + 1)
    
    return result

def find_anagrams_with_optimization(s, p):
    if len(p) > len(s):
        return []
    
    from collections import Counter
    
    p_count = Counter(p)
    window_count = Counter()
    result = []
    
    for i in range(len(s)):
        window_count[s[i]] += 1
        
        if i >= len(p):
            left_char = s[i - len(p)]
            if window_count[left_char] == 1:
                del window_count[left_char]
            else:
                window_count[left_char] -= 1
        
        if window_count == p_count:
            result.append(i - len(p) + 1)
    
    return result

def find_anagrams_with_advanced_optimization(s, p):
    if len(p) > len(s):
        return []
    
    from collections import Counter
    
    p_count = Counter(p)
    window_count = Counter()
    result = []
    
    for i in range(len(s)):
        window_count[s[i]] += 1
        
        if i >= len(p):
            left_char = s[i - len(p)]
            if window_count[left_char] == 1:
                del window_count[left_char]
            else:
                window_count[left_char] -= 1
        
        if window_count == p_count:
            result.append(i - len(p) + 1)
    
    return result

def find_anagrams_with_count(s, p):
    if len(p) > len(s):
        return [], 0
    
    from collections import Counter
    
    p_count = Counter(p)
    window_count = Counter()
    result = []
    count = 0
    
    for i in range(len(s)):
        window_count[s[i]] += 1
        
        if i >= len(p):
            left_char = s[i - len(p)]
            if window_count[left_char] == 1:
                del window_count[left_char]
            else:
                window_count[left_char] -= 1
        
        if window_count == p_count:
            result.append(i - len(p) + 1)
            count += 1
    
    return result, count

def find_anagrams_with_substrings(s, p):
    if len(p) > len(s):
        return [], []
    
    from collections import Counter
    
    p_count = Counter(p)
    window_count = Counter()
    result = []
    substrings = []
    
    for i in range(len(s)):
        window_count[s[i]] += 1
        
        if i >= len(p):
            left_char = s[i - len(p)]
            if window_count[left_char] == 1:
                del window_count[left_char]
            else:
                window_count[left_char] -= 1
        
        if window_count == p_count:
            result.append(i - len(p) + 1)
            substrings.append(s[i - len(p) + 1:i + 1])
    
    return result, substrings

def find_anagrams_with_negative(s, p):
    if len(p) > len(s):
        return []
    
    from collections import Counter
    
    p_count = Counter(p)
    window_count = Counter()
    result = []
    
    for i in range(len(s)):
        window_count[s[i]] += 1
        
        if i >= len(p):
            left_char = s[i - len(p)]
            if window_count[left_char] == 1:
                del window_count[left_char]
            else:
                window_count[left_char] -= 1
        
        if window_count == p_count:
            result.append(i - len(p) + 1)
    
    return result

def find_anagrams_with_circular(s, p):
    if len(p) > len(s):
        return []
    
    from collections import Counter
    
    p_count = Counter(p)
    window_count = Counter()
    result = []
    
    for i in range(2 * len(s)):
        window_count[s[i % len(s)]] += 1
        
        if i >= len(p):
            left_char = s[(i - len(p)) % len(s)]
            if window_count[left_char] == 1:
                del window_count[left_char]
            else:
                window_count[left_char] -= 1
        
        if window_count == p_count:
            result.append(i - len(p) + 1)
    
    return result

def find_anagrams_with_validation_enhanced(s, p):
    if not s or not p:
        return []
    
    if len(p) > len(s):
        return []
    
    from collections import Counter
    
    p_count = Counter(p)
    window_count = Counter()
    result = []
    
    for i in range(len(s)):
        window_count[s[i]] += 1
        
        if i >= len(p):
            left_char = s[i - len(p)]
            if window_count[left_char] == 1:
                del window_count[left_char]
            else:
                window_count[left_char] -= 1
        
        if window_count == p_count:
            result.append(i - len(p) + 1)
    
    return result

def find_anagrams_with_optimization_enhanced(s, p):
    if len(p) > len(s):
        return []
    
    from collections import Counter
    
    p_count = Counter(p)
    window_count = Counter()
    result = []
    
    for i in range(len(s)):
        window_count[s[i]] += 1
        
        if i >= len(p):
            left_char = s[i - len(p)]
            if window_count[left_char] == 1:
                del window_count[left_char]
            else:
                window_count[left_char] -= 1
        
        if window_count == p_count:
            result.append(i - len(p) + 1)
    
    return result

def find_anagrams_with_advanced_optimization_enhanced(s, p):
    if len(p) > len(s):
        return []
    
    from collections import Counter
    
    p_count = Counter(p)
    window_count = Counter()
    result = []
    
    for i in range(len(s)):
        window_count[s[i]] += 1
        
        if i >= len(p):
            left_char = s[i - len(p)]
            if window_count[left_char] == 1:
                del window_count[left_char]
            else:
                window_count[left_char] -= 1
        
        if window_count == p_count:
            result.append(i - len(p) + 1)
    
    return result

s = "cbaebabacd"
p = "abc"

anagrams1 = find_anagrams_brute_force(s, p)
anagrams2 = find_anagrams_sliding_window(s, p)
anagrams3 = find_anagrams_optimized(s, p)
anagrams4 = find_anagrams_with_validation(s, p)
anagrams5 = find_anagrams_with_optimization(s, p)
anagrams6 = find_anagrams_with_advanced_optimization(s, p)
anagrams7, count = find_anagrams_with_count(s, p)
anagrams8, substrings = find_anagrams_with_substrings(s, p)
anagrams9 = find_anagrams_with_negative(s, p)
anagrams10 = find_anagrams_with_circular(s, p)
anagrams11 = find_anagrams_with_validation_enhanced(s, p)
anagrams12 = find_anagrams_with_optimization_enhanced(s, p)
anagrams13 = find_anagrams_with_advanced_optimization_enhanced(s, p)

print(f"String: {s}")
print(f"Pattern: {p}")
print(f"Anagrams (brute force): {anagrams1}")
print(f"Anagrams (sliding window): {anagrams2}")
print(f"Anagrams (optimized): {anagrams3}")
print(f"Anagrams (with validation): {anagrams4}")
print(f"Anagrams (with optimization): {anagrams5}")
print(f"Anagrams (advanced optimization): {anagrams6}")
print(f"Anagrams (with count): {anagrams7}, Count: {count}")
print(f"Anagrams (with substrings): {anagrams8}, Substrings: {substrings}")
print(f"Anagrams (with negative): {anagrams9}")
print(f"Anagrams (with circular): {anagrams10}")
print(f"Anagrams (validation enhanced): {anagrams11}")
print(f"Anagrams (optimization enhanced): {anagrams12}")
print(f"Anagrams (advanced optimization enhanced): {anagrams13}")
