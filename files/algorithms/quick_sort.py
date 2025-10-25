def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

def quick_sort_inplace(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_inplace(arr, low, pi - 1)
        quick_sort_inplace(arr, pi + 1, high)
    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort_3_way(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        lt, gt = partition_3_way(arr, low, high)
        quick_sort_3_way(arr, low, lt - 1)
        quick_sort_3_way(arr, gt + 1, high)
    return arr

def partition_3_way(arr, low, high):
    pivot = arr[low]
    lt = low
    i = low
    gt = high
    
    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1
    
    return lt, gt

numbers = [10, 7, 8, 9, 1, 5]
print(f"Original: {numbers}")

sorted1 = quick_sort(numbers.copy())
sorted2 = quick_sort_inplace(numbers.copy())
sorted3 = quick_sort_3_way(numbers.copy())

print(f"Quick sort: {sorted1}")
print(f"Quick sort (in-place): {sorted2}")
print(f"Quick sort (3-way): {sorted3}")
