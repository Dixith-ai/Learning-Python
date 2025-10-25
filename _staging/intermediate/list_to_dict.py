def list_to_dict_index(lst):
    return {i: lst[i] for i in range(len(lst))}

def list_to_dict_value_count(lst):
    result = {}
    for item in lst:
        result[item] = result.get(item, 0) + 1
    return result

def list_to_dict_custom(lst, key_func):
    result = {}
    for item in lst:
        key = key_func(item)
        if key not in result:
            result[key] = []
        result[key].append(item)
    return result

numbers = [1, 2, 3, 4, 5]
words = ['apple', 'banana', 'apple', 'cherry', 'banana']

index_dict = list_to_dict_index(numbers)
count_dict = list_to_dict_value_count(words)
length_dict = list_to_dict_custom(words, len)

print(f"Numbers: {numbers}")
print(f"Index dict: {index_dict}")

print(f"Words: {words}")
print(f"Count dict: {count_dict}")
print(f"Length dict: {length_dict}")
