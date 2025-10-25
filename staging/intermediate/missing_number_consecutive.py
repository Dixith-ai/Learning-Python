def find_missing_consecutive(lst):
    if not lst:
        return None
    
    min_val = min(lst)
    max_val = max(lst)
    expected_sum = sum(range(min_val, max_val + 1))
    actual_sum = sum(lst)
    
    return expected_sum - actual_sum

def find_missing_consecutive_xor(lst):
    if not lst:
        return None
    
    min_val = min(lst)
    max_val = max(lst)
    
    xor_all = 0
    for i in range(min_val, max_val + 1):
        xor_all ^= i
    
    xor_lst = 0
    for num in lst:
        xor_lst ^= num
    
    return xor_all ^ xor_lst

def find_all_missing_consecutive(lst):
    if not lst:
        return []
    
    min_val = min(lst)
    max_val = max(lst)
    lst_set = set(lst)
    
    missing = []
    for i in range(min_val, max_val + 1):
        if i not in lst_set:
            missing.append(i)
    
    return missing

numbers = [1, 2, 4, 5, 6, 8, 9]
missing = find_missing_consecutive(numbers)
missing_xor = find_missing_consecutive_xor(numbers)
all_missing = find_all_missing_consecutive(numbers)

print(f"List: {numbers}")
print(f"Missing number: {missing}")
print(f"Missing number (XOR): {missing_xor}")
print(f"All missing numbers: {all_missing}")
