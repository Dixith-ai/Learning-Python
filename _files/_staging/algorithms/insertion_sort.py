def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def insertion_sort_binary(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        pos = binary_search_position(arr, key, 0, i - 1)
        for j in range(i, pos, -1):
            arr[j] = arr[j - 1]
        arr[pos] = key
    return arr

def binary_search_position(arr, key, left, right):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid + 1
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return left

def insertion_sort_recursive(arr, n=None):
    if n is None:
        n = len(arr)
    
    if n <= 1:
        return arr
    
    insertion_sort_recursive(arr, n - 1)
    
    last = arr[n - 1]
    j = n - 2
    
    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j -= 1
    
    arr[j + 1] = last
    return arr

numbers = [12, 11, 13, 5, 6]
print(f"Original: {numbers}")

sorted1 = insertion_sort(numbers.copy())
sorted2 = insertion_sort_binary(numbers.copy())
sorted3 = insertion_sort_recursive(numbers.copy())

print(f"Insertion sort: {sorted1}")
print(f"Insertion sort (binary): {sorted2}")
print(f"Insertion sort (recursive): {sorted3}")
