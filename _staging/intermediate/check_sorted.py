def is_sorted_ascending(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

def is_sorted_descending(lst):
    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            return False
    return True

def is_sorted(lst):
    return is_sorted_ascending(lst) or is_sorted_descending(lst)

sorted_list = [1, 2, 3, 4, 5]
unsorted_list = [3, 1, 4, 2, 5]
descending_list = [5, 4, 3, 2, 1]

print(f"{sorted_list} is sorted: {is_sorted(sorted_list)}")
print(f"{unsorted_list} is sorted: {is_sorted(unsorted_list)}")
print(f"{descending_list} is sorted: {is_sorted(descending_list)}")
