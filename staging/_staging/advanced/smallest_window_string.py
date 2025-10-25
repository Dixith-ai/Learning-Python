def smallest_window_brute_force(s, t):
    if not s or not t:
        return ""
    
    min_len = float('inf')
    min_window = ""
    
    for i in range(len(s)):
        for j in range(i + len(t), len(s) + 1):
            window = s[i:j]
            if all(window.count(c) >= t.count(c) for c in set(t)):
                if len(window) < min_len:
                    min_len = len(window)
                    min_window = window
    
    return min_window

def smallest_window_sliding_window(s, t):
    if not s or not t:
        return ""
    
    from collections import Counter
    
    t_count = Counter(t)
    required = len(t_count)
    
    left = 0
    formed = 0
    window_counts = {}
    
    ans = float('inf'), None, None
    
    for right in range(len(s)):
        c = s[right]
        window_counts[c] = window_counts.get(c, 0) + 1
        
        if c in t_count and window_counts[c] == t_count[c]:
            formed += 1
        
        while left <= right and formed == required:
            c = s[left]
            
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)
            
            window_counts[c] -= 1
            if c in t_count and window_counts[c] < t_count[c]:
                formed -= 1
            
            left += 1
    
    return "" if ans[0] == float('inf') else s[ans[1]:ans[2] + 1]

def smallest_window_optimized(s, t):
    if not s or not t:
        return ""
    
    from collections import Counter
    
    t_count = Counter(t)
    required = len(t_count)
    
    left = 0
    formed = 0
    window_counts = {}
    
    ans = float('inf'), None, None
    
    for right in range(len(s)):
        c = s[right]
        window_counts[c] = window_counts.get(c, 0) + 1
        
        if c in t_count and window_counts[c] == t_count[c]:
            formed += 1
        
        while left <= right and formed == required:
            c = s[left]
            
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)
            
            window_counts[c] -= 1
            if c in t_count and window_counts[c] < t_count[c]:
                formed -= 1
            
            left += 1
    
    return "" if ans[0] == float('inf') else s[ans[1]:ans[2] + 1]

def smallest_window_with_validation(s, t):
    if not s or not t:
        return ""
    
    if len(t) > len(s):
        return ""
    
    from collections import Counter
    
    t_count = Counter(t)
    required = len(t_count)
    
    left = 0
    formed = 0
    window_counts = {}
    
    ans = float('inf'), None, None
    
    for right in range(len(s)):
        c = s[right]
        window_counts[c] = window_counts.get(c, 0) + 1
        
        if c in t_count and window_counts[c] == t_count[c]:
            formed += 1
        
        while left <= right and formed == required:
            c = s[left]
            
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)
            
            window_counts[c] -= 1
            if c in t_count and window_counts[c] < t_count[c]:
                formed -= 1
            
            left += 1
    
    return "" if ans[0] == float('inf') else s[ans[1]:ans[2] + 1]

def smallest_window_with_constraints(s, t, constraints):
    if not s or not t:
        return ""
    
    from collections import Counter
    
    t_count = Counter(t)
    required = len(t_count)
    
    left = 0
    formed = 0
    window_counts = {}
    
    ans = float('inf'), None, None
    
    for right in range(len(s)):
        c = s[right]
        if constraints(c):
            window_counts[c] = window_counts.get(c, 0) + 1
            
            if c in t_count and window_counts[c] == t_count[c]:
                formed += 1
            
            while left <= right and formed == required:
                c = s[left]
                
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                
                window_counts[c] -= 1
                if c in t_count and window_counts[c] < t_count[c]:
                    formed -= 1
                
                left += 1
    
    return "" if ans[0] == float('inf') else s[ans[1]:ans[2] + 1]

def smallest_window_with_optimization(s, t):
    if not s or not t:
        return ""
    
    from collections import Counter
    
    t_count = Counter(t)
    required = len(t_count)
    
    left = 0
    formed = 0
    window_counts = {}
    
    ans = float('inf'), None, None
    
    for right in range(len(s)):
        c = s[right]
        window_counts[c] = window_counts.get(c, 0) + 1
        
        if c in t_count and window_counts[c] == t_count[c]:
            formed += 1
        
        while left <= right and formed == required:
            c = s[left]
            
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)
            
            window_counts[c] -= 1
            if c in t_count and window_counts[c] < t_count[c]:
                formed -= 1
            
            left += 1
    
    return "" if ans[0] == float('inf') else s[ans[1]:ans[2] + 1]

def smallest_window_with_advanced_optimization(s, t):
    if not s or not t:
        return ""
    
    from collections import Counter
    
    t_count = Counter(t)
    required = len(t_count)
    
    left = 0
    formed = 0
    window_counts = {}
    
    ans = float('inf'), None, None
    
    for right in range(len(s)):
        c = s[right]
        window_counts[c] = window_counts.get(c, 0) + 1
        
        if c in t_count and window_counts[c] == t_count[c]:
            formed += 1
        
        while left <= right and formed == required:
            c = s[left]
            
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)
            
            window_counts[c] -= 1
            if c in t_count and window_counts[c] < t_count[c]:
                formed -= 1
            
            left += 1
    
    return "" if ans[0] == float('inf') else s[ans[1]:ans[2] + 1]

def smallest_window_with_count(s, t):
    if not s or not t:
        return "", 0
    
    from collections import Counter
    
    t_count = Counter(t)
    required = len(t_count)
    
    left = 0
    formed = 0
    window_counts = {}
    count = 0
    
    ans = float('inf'), None, None
    
    for right in range(len(s)):
        c = s[right]
        window_counts[c] = window_counts.get(c, 0) + 1
        
        if c in t_count and window_counts[c] == t_count[c]:
            formed += 1
        
        while left <= right and formed == required:
            c = s[left]
            
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)
                count = 1
            elif right - left + 1 == ans[0]:
                count += 1
            
            window_counts[c] -= 1
            if c in t_count and window_counts[c] < t_count[c]:
                formed -= 1
            
            left += 1
    
    return ("" if ans[0] == float('inf') else s[ans[1]:ans[2] + 1]), count

def smallest_window_with_all_windows(s, t):
    if not s or not t:
        return "", []
    
    from collections import Counter
    
    t_count = Counter(t)
    required = len(t_count)
    
    left = 0
    formed = 0
    window_counts = {}
    all_windows = []
    
    ans = float('inf'), None, None
    
    for right in range(len(s)):
        c = s[right]
        window_counts[c] = window_counts.get(c, 0) + 1
        
        if c in t_count and window_counts[c] == t_count[c]:
            formed += 1
        
        while left <= right and formed == required:
            c = s[left]
            
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)
                all_windows = [s[left:right + 1]]
            elif right - left + 1 == ans[0]:
                all_windows.append(s[left:right + 1])
            
            window_counts[c] -= 1
            if c in t_count and window_counts[c] < t_count[c]:
                formed -= 1
            
            left += 1
    
    return ("" if ans[0] == float('inf') else s[ans[1]:ans[2] + 1]), all_windows

s = "ADOBECODEBANC"
t = "ABC"

window1 = smallest_window_brute_force(s, t)
window2 = smallest_window_sliding_window(s, t)
window3 = smallest_window_optimized(s, t)
window4 = smallest_window_with_validation(s, t)
window5 = smallest_window_with_optimization(s, t)
window6 = smallest_window_with_advanced_optimization(s, t)
window7, count = smallest_window_with_count(s, t)
window8, all_windows = smallest_window_with_all_windows(s, t)

print(f"String: {s}")
print(f"Target: {t}")
print(f"Smallest window (brute force): {window1}")
print(f"Smallest window (sliding window): {window2}")
print(f"Smallest window (optimized): {window3}")
print(f"Smallest window (with validation): {window4}")
print(f"Smallest window (with optimization): {window5}")
print(f"Smallest window (advanced optimization): {window6}")
print(f"Smallest window (with count): {window7}, Count: {count}")
print(f"Smallest window (with all windows): {window8}, All windows: {all_windows}")
