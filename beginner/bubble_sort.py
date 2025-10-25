def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def bubble_sort_optimized(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def bubble_sort_recursive(arr, n=None):
    if n is None:
        n = len(arr)
    
    if n == 1:
        return arr
    
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    return bubble_sort_recursive(arr, n - 1)

numbers = [64, 34, 25, 12, 22, 11, 90]
print(f"Original: {numbers}")

sorted1 = bubble_sort(numbers.copy())
sorted2 = bubble_sort_optimized(numbers.copy())
sorted3 = bubble_sort_recursive(numbers.copy())

print(f"Bubble sort: {sorted1}")
print(f"Bubble sort (optimized): {sorted2}")
print(f"Bubble sort (recursive): {sorted3}")
