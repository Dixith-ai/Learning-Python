def find_intersection_hash_set(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    return list(set1.intersection(set2))

def find_intersection_hash_map(arr1, arr2):
    from collections import Counter
    
    count1 = Counter(arr1)
    count2 = Counter(arr2)
    
    intersection = []
    for num in count1:
        if num in count2:
            intersection.extend([num] * min(count1[num], count2[num]))
    
    return intersection

def find_intersection_brute_force(arr1, arr2):
    intersection = []
    
    for num in arr1:
        if num in arr2 and num not in intersection:
            intersection.append(num)
    
    return intersection

def find_intersection_sorted_arrays(arr1, arr2):
    arr1.sort()
    arr2.sort()
    
    i = j = 0
    intersection = []
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            if not intersection or intersection[-1] != arr1[i]:
                intersection.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    
    return intersection

def find_intersection_with_duplicates(arr1, arr2):
    from collections import Counter
    
    count1 = Counter(arr1)
    count2 = Counter(arr2)
    
    intersection = []
    for num in count1:
        if num in count2:
            intersection.extend([num] * min(count1[num], count2[num]))
    
    return intersection

def find_intersection_optimized(arr1, arr2):
    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1
    
    set1 = set(arr1)
    intersection = []
    
    for num in arr2:
        if num in set1:
            intersection.append(num)
            set1.remove(num)
    
    return intersection

def find_intersection_with_count(arr1, arr2):
    from collections import defaultdict
    
    count1 = defaultdict(int)
    count2 = defaultdict(int)
    
    for num in arr1:
        count1[num] += 1
    
    for num in arr2:
        count2[num] += 1
    
    intersection = []
    for num in count1:
        if num in count2:
            intersection.extend([num] * min(count1[num], count2[num]))
    
    return intersection

def find_intersection_using_dict(arr1, arr2):
    dict1 = {}
    for num in arr1:
        dict1[num] = dict1.get(num, 0) + 1
    
    intersection = []
    for num in arr2:
        if num in dict1 and dict1[num] > 0:
            intersection.append(num)
            dict1[num] -= 1
    
    return intersection

def find_intersection_with_frequency(arr1, arr2):
    from collections import Counter
    
    freq1 = Counter(arr1)
    freq2 = Counter(arr2)
    
    intersection = []
    for num in freq1:
        if num in freq2:
            intersection.extend([num] * min(freq1[num], freq2[num]))
    
    return intersection

arr1 = [1, 2, 2, 1]
arr2 = [2, 2]
arr3 = [4, 9, 5]
arr4 = [9, 4, 9, 8, 4]

intersection1 = find_intersection_hash_set(arr1, arr2)
intersection2 = find_intersection_hash_map(arr1, arr2)
intersection3 = find_intersection_brute_force(arr1, arr2)
intersection4 = find_intersection_sorted_arrays(arr1, arr2)
intersection5 = find_intersection_with_duplicates(arr1, arr2)
intersection6 = find_intersection_optimized(arr1, arr2)
intersection7 = find_intersection_with_count(arr1, arr2)
intersection8 = find_intersection_using_dict(arr1, arr2)
intersection9 = find_intersection_with_frequency(arr1, arr2)

print(f"Array 1: {arr1}")
print(f"Array 2: {arr2}")
print(f"Intersection (HashSet): {intersection1}")
print(f"Intersection (HashMap): {intersection2}")
print(f"Intersection (Brute force): {intersection3}")
print(f"Intersection (Sorted): {intersection4}")
print(f"Intersection (With duplicates): {intersection5}")
print(f"Intersection (Optimized): {intersection6}")
print(f"Intersection (With count): {intersection7}")
print(f"Intersection (Using dict): {intersection8}")
print(f"Intersection (With frequency): {intersection9}")

intersection10 = find_intersection_hash_set(arr3, arr4)
print(f"Array 3: {arr3}")
print(f"Array 4: {arr4}")
print(f"Intersection: {intersection10}")
