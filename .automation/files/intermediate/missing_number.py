def find_missing_number(lst):
    if not lst:
        return None
    
    n = len(lst) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(lst)
    
    return expected_sum - actual_sum

def find_missing_number_xor(lst):
    n = len(lst) + 1
    xor_all = 0
    xor_lst = 0
    
    for i in range(1, n + 1):
        xor_all ^= i
    
    for num in lst:
        xor_lst ^= num
    
    return xor_all ^ xor_lst

numbers = [1, 2, 4, 5, 6]
missing = find_missing_number(numbers)
missing_xor = find_missing_number_xor(numbers)

print(f"List: {numbers}")
print(f"Missing number: {missing}")
print(f"Missing number (XOR): {missing_xor}")
