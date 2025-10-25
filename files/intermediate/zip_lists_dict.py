def zip_lists_to_dict(keys, values):
    return dict(zip(keys, values))

def zip_lists_to_dict_loop(keys, values):
    result = {}
    for i in range(min(len(keys), len(values))):
        result[keys[i]] = values[i]
    return result

def zip_lists_to_dict_longest(keys, values):
    result = {}
    max_len = max(len(keys), len(values))
    
    for i in range(max_len):
        key = keys[i] if i < len(keys) else f"key_{i}"
        value = values[i] if i < len(values) else None
        result[key] = value
    
    return result

keys = ['a', 'b', 'c']
values = [1, 2, 3]

zipped_dict = zip_lists_to_dict(keys, values)
zipped_loop = zip_lists_to_dict_loop(keys, values)

print(f"Keys: {keys}")
print(f"Values: {values}")
print(f"Zipped dict: {zipped_dict}")
print(f"Zipped dict (loop): {zipped_loop}")

keys_long = ['x', 'y']
values_long = [10, 20, 30, 40]
zipped_longest = zip_lists_to_dict_longest(keys_long, values_long)
print(f"Longest zip: {zipped_longest}")
