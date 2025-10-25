def most_frequent_element_counter(arr):
    from collections import Counter
    counter = Counter(arr)
    return counter.most_common(1)[0][0]

def most_frequent_element_dict(arr):
    frequency = {}
    for element in arr:
        frequency[element] = frequency.get(element, 0) + 1
    
    max_freq = 0
    most_frequent = None
    for element, freq in frequency.items():
        if freq > max_freq:
            max_freq = freq
            most_frequent = element
    
    return most_frequent

def most_frequent_element_sort(arr):
    if not arr:
        return None
    
    arr.sort()
    current_element = arr[0]
    current_count = 1
    max_count = 1
    most_frequent = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] == current_element:
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
                most_frequent = current_element
            current_element = arr[i]
            current_count = 1
    
    if current_count > max_count:
        most_frequent = current_element
    
    return most_frequent

def most_frequent_element_brute_force(arr):
    if not arr:
        return None
    
    max_count = 0
    most_frequent = arr[0]
    
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1
        
        if count > max_count:
            max_count = count
            most_frequent = arr[i]
    
    return most_frequent

def most_frequent_element_with_count(arr):
    from collections import Counter
    counter = Counter(arr)
    most_common = counter.most_common(1)[0]
    return most_common[0], most_common[1]

def most_frequent_element_with_validation(arr):
    if not arr:
        return None
    
    if len(arr) == 1:
        return arr[0]
    
    frequency = {}
    for element in arr:
        frequency[element] = frequency.get(element, 0) + 1
    
    max_freq = max(frequency.values())
    most_frequent = [k for k, v in frequency.items() if v == max_freq]
    
    return most_frequent[0] if len(most_frequent) == 1 else most_frequent

def most_frequent_element_with_constraints(arr, constraints):
    frequency = {}
    for element in arr:
        if constraints(element):
            frequency[element] = frequency.get(element, 0) + 1
    
    if not frequency:
        return None
    
    max_freq = max(frequency.values())
    most_frequent = [k for k, v in frequency.items() if v == max_freq]
    
    return most_frequent[0]

def most_frequent_element_with_optimization(arr):
    if not arr:
        return None
    
    frequency = {}
    max_freq = 0
    most_frequent = None
    
    for element in arr:
        frequency[element] = frequency.get(element, 0) + 1
        if frequency[element] > max_freq:
            max_freq = frequency[element]
            most_frequent = element
    
    return most_frequent

def most_frequent_element_with_advanced_optimization(arr):
    if not arr:
        return None
    
    frequency = {}
    max_freq = 0
    most_frequent = None
    
    for element in arr:
        frequency[element] = frequency.get(element, 0) + 1
        if frequency[element] > max_freq:
            max_freq = frequency[element]
            most_frequent = element
    
    return most_frequent

def most_frequent_element_with_multiple(arr):
    from collections import Counter
    counter = Counter(arr)
    max_freq = max(counter.values())
    most_frequent = [k for k, v in counter.items() if v == max_freq]
    
    return most_frequent

arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

frequent1 = most_frequent_element_counter(arr)
frequent2 = most_frequent_element_dict(arr)
frequent3 = most_frequent_element_sort(arr)
frequent4 = most_frequent_element_brute_force(arr)
frequent5, count = most_frequent_element_with_count(arr)
frequent6 = most_frequent_element_with_validation(arr)
frequent7 = most_frequent_element_with_optimization(arr)
frequent8 = most_frequent_element_with_advanced_optimization(arr)
frequent9 = most_frequent_element_with_multiple(arr)

print(f"Array: {arr}")
print(f"Most frequent (Counter): {frequent1}")
print(f"Most frequent (dict): {frequent2}")
print(f"Most frequent (sort): {frequent3}")
print(f"Most frequent (brute force): {frequent4}")
print(f"Most frequent (with count): {frequent5}, Count: {count}")
print(f"Most frequent (with validation): {frequent6}")
print(f"Most frequent (with optimization): {frequent7}")
print(f"Most frequent (advanced optimization): {frequent8}")
print(f"Most frequent (multiple): {frequent9}")
