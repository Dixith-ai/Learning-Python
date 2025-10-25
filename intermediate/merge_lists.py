def merge_lists(list1, list2):
    return list1 + list2

def merge_lists_extend(list1, list2):
    result = list1.copy()
    result.extend(list2)
    return result

def merge_lists_unique(list1, list2):
    return list(set(list1 + list2))

list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged = merge_lists(list1, list2)
merged_extend = merge_lists_extend(list1, list2)
print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Merged: {merged}")
print(f"Merged with extend: {merged_extend}")

list3 = [1, 2, 3, 4]
list4 = [3, 4, 5, 6]
merged_unique = merge_lists_unique(list3, list4)
print(f"Unique merge: {merged_unique}")
