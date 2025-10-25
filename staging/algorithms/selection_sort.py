def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def selection_sort_stable(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            min_val = arr[min_idx]
            for k in range(min_idx, i, -1):
                arr[k] = arr[k - 1]
            arr[i] = min_val
    return arr

def selection_sort_recursive(arr, start=0):
    if start >= len(arr) - 1:
        return arr
    
    min_idx = start
    for i in range(start + 1, len(arr)):
        if arr[i] < arr[min_idx]:
            min_idx = i
    
    if min_idx != start:
        arr[start], arr[min_idx] = arr[min_idx], arr[start]
    
    return selection_sort_recursive(arr, start + 1)

numbers = [64, 25, 12, 22, 11]
print(f"Original: {numbers}")

sorted1 = selection_sort(numbers.copy())
sorted2 = selection_sort_stable(numbers.copy())
sorted3 = selection_sort_recursive(numbers.copy())

print(f"Selection sort: {sorted1}")
print(f"Selection sort (stable): {sorted2}")
print(f"Selection sort (recursive): {sorted3}")
