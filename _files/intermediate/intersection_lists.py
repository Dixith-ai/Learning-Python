def find_intersection_set(list1, list2):
    return list(set(list1) & set(list2))

def find_intersection_loop(list1, list2):
    intersection = []
    for item in list1:
        if item in list2 and item not in intersection:
            intersection.append(item)
    return intersection

def find_intersection_sorted(list1, list2):
    list1_sorted = sorted(list1)
    list2_sorted = sorted(list2)
    
    i = j = 0
    intersection = []
    
    while i < len(list1_sorted) and j < len(list2_sorted):
        if list1_sorted[i] == list2_sorted[j]:
            if not intersection or intersection[-1] != list1_sorted[i]:
                intersection.append(list1_sorted[i])
            i += 1
            j += 1
        elif list1_sorted[i] < list2_sorted[j]:
            i += 1
        else:
            j += 1
    
    return intersection

def find_intersection_with_count(list1, list2):
    from collections import Counter
    count1 = Counter(list1)
    count2 = Counter(list2)
    
    intersection = []
    for item in count1:
        if item in count2:
            intersection.extend([item] * min(count1[item], count2[item]))
    
    return intersection

list1 = [1, 2, 2, 3, 4]
list2 = [2, 3, 3, 4, 5]

intersection1 = find_intersection_set(list1, list2)
intersection2 = find_intersection_loop(list1, list2)
intersection3 = find_intersection_sorted(list1, list2)
intersection4 = find_intersection_with_count(list1, list2)

print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Intersection (set): {intersection1}")
print(f"Intersection (loop): {intersection2}")
print(f"Intersection (sorted): {intersection3}")
print(f"Intersection (with count): {intersection4}")
