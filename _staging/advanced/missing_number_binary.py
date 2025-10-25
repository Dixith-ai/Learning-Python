def find_missing_number_binary(arr):
    n = len(arr)
    left, right = 0, n - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == mid + 1:
            left = mid + 1
        else:
            right = mid - 1
    
    return left + 1

def find_missing_number_binary_alternative(arr):
    n = len(arr)
    left, right = 0, n
    
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] == mid + 1:
            left = mid + 1
        else:
            right = mid
    
    return left + 1

def find_missing_number_binary_recursive(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return left + 1
    
    mid = (left + right) // 2
    
    if arr[mid] == mid + 1:
        return find_missing_number_binary_recursive(arr, mid + 1, right)
    else:
        return find_missing_number_binary_recursive(arr, left, mid - 1)

def find_multiple_missing_numbers_binary(arr):
    missing = []
    n = len(arr)
    
    for i in range(n):
        if arr[i] != i + 1:
            missing.append(i + 1)
    
    return missing

arr1 = [1, 2, 3, 5, 6, 7, 8]
arr2 = [1, 2, 4, 5, 6, 7, 8, 9]

missing1 = find_missing_number_binary(arr1)
missing2 = find_missing_number_binary_alternative(arr2)
missing3 = find_missing_number_binary_recursive(arr1)
missing4 = find_multiple_missing_numbers_binary([1, 2, 4, 6, 7, 9])

print(f"Array 1: {arr1}")
print(f"Missing number: {missing1}")
print(f"Array 2: {arr2}")
print(f"Missing number (alternative): {missing2}")
print(f"Missing number (recursive): {missing3}")
print(f"Multiple missing: {missing4}")
