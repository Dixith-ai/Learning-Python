def find_kth_largest_sort(lst, k):
    if k > len(lst) or k <= 0:
        return None
    return sorted(lst, reverse=True)[k-1]

def find_kth_largest_heap(lst, k):
    import heapq
    if k > len(lst) or k <= 0:
        return None
    return heapq.nlargest(k, lst)[-1]

def find_kth_largest_quickselect(lst, k):
    if k > len(lst) or k <= 0:
        return None
    
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if arr[j] >= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    def quickselect(arr, low, high, k):
        if low <= high:
            pi = partition(arr, low, high)
            
            if pi == k - 1:
                return arr[pi]
            elif pi > k - 1:
                return quickselect(arr, low, pi - 1, k)
            else:
                return quickselect(arr, pi + 1, high, k)
        
        return None
    
    arr = lst.copy()
    return quickselect(arr, 0, len(arr) - 1, k)

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
k = 3

kth_sort = find_kth_largest_sort(numbers, k)
kth_heap = find_kth_largest_heap(numbers, k)
kth_quick = find_kth_largest_quickselect(numbers, k)

print(f"List: {numbers}")
print(f"{k}th largest (sort): {kth_sort}")
print(f"{k}th largest (heap): {kth_heap}")
print(f"{k}th largest (quickselect): {kth_quick}")
