def flatten_list_recursive(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_list_recursive(item))
        else:
            result.append(item)
    return result

def flatten_list_iterative(lst):
    result = []
    stack = lst[:]
    
    while stack:
        item = stack.pop()
        if isinstance(item, list):
            stack.extend(item)
        else:
            result.append(item)
    
    return result[::-1]

nested_list = [1, [2, 3], [4, [5, 6]], 7]

flattened_recursive = flatten_list_recursive(nested_list)
flattened_iterative = flatten_list_iterative(nested_list)

print(f"Nested list: {nested_list}")
print(f"Flattened (recursive): {flattened_recursive}")
print(f"Flattened (iterative): {flattened_iterative}")
