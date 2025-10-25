def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

def find_common_elements_loop(list1, list2):
    common = []
    for item in list1:
        if item in list2 and item not in common:
            common.append(item)
    return common

def find_common_elements_count(list1, list2):
    common = []
    for item in set(list1):
        if item in list2:
            common.append(item)
    return common

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common = find_common_elements(list1, list2)
common_loop = find_common_elements_loop(list1, list2)

print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Common elements: {common}")
print(f"Common elements (loop): {common_loop}")
