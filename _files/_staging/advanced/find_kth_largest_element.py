def find_kth_largest_sort(nums, k):
    nums.sort(reverse=True)
    return nums[k - 1]

def find_kth_largest_heap(nums, k):
    import heapq
    heap = []
    
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    
    return heap[0]

def find_kth_largest_quickselect(nums, k):
    def partition(left, right, pivot_index):
        pivot = nums[pivot_index]
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        
        store_index = left
        for i in range(left, right):
            if nums[i] > pivot:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1
        
        nums[right], nums[store_index] = nums[store_index], nums[right]
        return store_index
    
    def quickselect(left, right, k_smallest):
        if left == right:
            return nums[left]
        
        pivot_index = partition(left, right, left)
        
        if k_smallest == pivot_index:
            return nums[k_smallest]
        elif k_smallest < pivot_index:
            return quickselect(left, pivot_index - 1, k_smallest)
        else:
            return quickselect(pivot_index + 1, right, k_smallest)
    
    return quickselect(0, len(nums) - 1, k - 1)

def find_kth_largest_optimized(nums, k):
    import heapq
    heap = []
    
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    
    return heap[0]

def find_kth_largest_with_validation(nums, k):
    if not nums or k <= 0 or k > len(nums):
        return None
    
    import heapq
    heap = []
    
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    
    return heap[0]

def find_kth_largest_with_constraints(nums, k, constraints):
    import heapq
    heap = []
    
    for num in nums:
        if constraints(num):
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
    
    return heap[0] if heap else None

def find_kth_largest_with_optimization(nums, k):
    import heapq
    heap = []
    
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    
    return heap[0]

def find_kth_largest_with_advanced_optimization(nums, k):
    import heapq
    heap = []
    
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    
    return heap[0]

def find_kth_largest_with_count(nums, k):
    import heapq
    heap = []
    count = 0
    
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
        count += 1
    
    return heap[0], count

def find_kth_largest_with_multiple(nums, k):
    import heapq
    heap = []
    
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    
    return heap[0]

def find_kth_largest_with_negative(nums, k):
    import heapq
    heap = []
    
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    
    return heap[0]

def find_kth_largest_with_circular(nums, k):
    import heapq
    heap = []
    
    for i in range(2 * len(nums)):
        num = nums[i % len(nums)]
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    
    return heap[0]

def find_kth_largest_with_validation_enhanced(nums, k):
    if not nums or k <= 0 or k > len(nums):
        return None
    
    if k == 1:
        return max(nums)
    
    if k == len(nums):
        return min(nums)
    
    import heapq
    heap = []
    
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    
    return heap[0]

def find_kth_largest_with_optimization_enhanced(nums, k):
    import heapq
    heap = []
    
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    
    return heap[0]

def find_kth_largest_with_advanced_optimization_enhanced(nums, k):
    import heapq
    heap = []
    
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    
    return heap[0]

def find_kth_largest_with_statistics(nums, k):
    import heapq
    heap = []
    count = 0
    sum_nums = 0
    
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
        count += 1
        sum_nums += num
    
    return heap[0], {
        'count': count,
        'sum': sum_nums,
        'k': k
    }

def find_kth_largest_with_advanced_features(nums, k):
    import heapq
    heap = []
    count = 0
    sum_nums = 0
    min_val = float('inf')
    max_val = float('-inf')
    
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
        count += 1
        sum_nums += num
        min_val = min(min_val, num)
        max_val = max(max_val, num)
    
    return heap[0], {
        'count': count,
        'sum': sum_nums,
        'k': k,
        'min': min_val,
        'max': max_val
    }

nums = [3, 2, 1, 5, 6, 4]
k = 2

kth1 = find_kth_largest_sort(nums, k)
kth2 = find_kth_largest_heap(nums, k)
kth3 = find_kth_largest_quickselect(nums, k)
kth4 = find_kth_largest_optimized(nums, k)
kth5 = find_kth_largest_with_validation(nums, k)
kth6 = find_kth_largest_with_optimization(nums, k)
kth7 = find_kth_largest_with_advanced_optimization(nums, k)
kth8, count = find_kth_largest_with_count(nums, k)
kth9 = find_kth_largest_with_multiple(nums, k)
kth10 = find_kth_largest_with_negative(nums, k)
kth11 = find_kth_largest_with_circular(nums, k)
kth12 = find_kth_largest_with_validation_enhanced(nums, k)
kth13 = find_kth_largest_with_optimization_enhanced(nums, k)
kth14 = find_kth_largest_with_advanced_optimization_enhanced(nums, k)
kth15, stats = find_kth_largest_with_statistics(nums, k)
kth16, features = find_kth_largest_with_advanced_features(nums, k)

print(f"Array: {nums}")
print(f"K: {k}")
print(f"Kth largest (sort): {kth1}")
print(f"Kth largest (heap): {kth2}")
print(f"Kth largest (quickselect): {kth3}")
print(f"Kth largest (optimized): {kth4}")
print(f"Kth largest (with validation): {kth5}")
print(f"Kth largest (with optimization): {kth6}")
print(f"Kth largest (advanced optimization): {kth7}")
print(f"Kth largest (with count): {kth8}, Count: {count}")
print(f"Kth largest (with multiple): {kth9}")
print(f"Kth largest (with negative): {kth10}")
print(f"Kth largest (with circular): {kth11}")
print(f"Kth largest (validation enhanced): {kth12}")
print(f"Kth largest (optimization enhanced): {kth13}")
print(f"Kth largest (advanced optimization enhanced): {kth14}")
print(f"Kth largest (with statistics): {kth15}, Statistics: {stats}")
print(f"Kth largest (with advanced features): {kth16}, Features: {features}")
