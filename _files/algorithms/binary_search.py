def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def binary_search_recursive(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

def binary_search_first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

def binary_search_last_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6

result1 = binary_search_iterative(arr, target)
result2 = binary_search_recursive(arr, target)
result3 = binary_search_first_occurrence([1, 2, 2, 2, 3, 4], 2)
result4 = binary_search_last_occurrence([1, 2, 2, 2, 3, 4], 2)

print(f"Array: {arr}")
print(f"Target: {target}")
print(f"Binary search (iterative): {result1}")
print(f"Binary search (recursive): {result2}")
print(f"First occurrence of 2: {result3}")
print(f"Last occurrence of 2: {result4}")
