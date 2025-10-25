def flatten_dict(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def flatten_dict_iterative(d, sep='_'):
    stack = [(k, v) for k, v in d.items()]
    result = {}
    
    while stack:
        key, value = stack.pop()
        if isinstance(value, dict):
            for k, v in value.items():
                stack.append((f"{key}{sep}{k}", v))
        else:
            result[key] = value
    
    return result

nested_dict = {
    'a': 1,
    'b': {
        'c': 2,
        'd': {
            'e': 3,
            'f': 4
        }
    },
    'g': 5
}

flattened_recursive = flatten_dict(nested_dict)
flattened_iterative = flatten_dict_iterative(nested_dict)

print(f"Nested dict: {nested_dict}")
print(f"Flattened (recursive): {flattened_recursive}")
print(f"Flattened (iterative): {flattened_iterative}")
