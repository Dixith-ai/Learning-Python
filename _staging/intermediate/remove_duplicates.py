def remove_duplicates_set(lst):
    return list(set(lst))

def remove_duplicates_loop(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

def remove_duplicates_dict(lst):
    return list(dict.fromkeys(lst))

numbers = [1, 2, 2, 3, 4, 4, 5, 1]
unique_set = remove_duplicates_set(numbers)
unique_loop = remove_duplicates_loop(numbers)
unique_dict = remove_duplicates_dict(numbers)

print(f"Original: {numbers}")
print(f"Unique (set): {unique_set}")
print(f"Unique (loop): {unique_loop}")
print(f"Unique (dict): {unique_dict}")
