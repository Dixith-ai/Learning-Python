def kth_smallest_matrix_brute_force(matrix, k):
    flattened = []
    for row in matrix:
        flattened.extend(row)
    flattened.sort()
    return flattened[k - 1]

def kth_smallest_matrix_heap(matrix, k):
    import heapq
    heap = []
    
    for row in matrix:
        for num in row:
            heapq.heappush(heap, num)
    
    for _ in range(k - 1):
        heapq.heappop(heap)
    
    return heap[0]

def kth_smallest_matrix_binary_search(matrix, k):
    def count_less_equal(target):
        count = 0
        row, col = len(matrix) - 1, 0
        
        while row >= 0 and col < len(matrix[0]):
            if matrix[row][col] <= target:
                count += row + 1
                col += 1
            else:
                row -= 1
        
        return count
    
    left = matrix[0][0]
    right = matrix[-1][-1]
    
    while left < right:
        mid = (left + right) // 2
        count = count_less_equal(mid)
        
        if count < k:
            left = mid + 1
        else:
            right = mid
    
    return left

def kth_smallest_matrix_optimized(matrix, k):
    import heapq
    heap = []
    
    for row in matrix:
        for num in row:
            heapq.heappush(heap, num)
    
    for _ in range(k - 1):
        heapq.heappop(heap)
    
    return heap[0]

def kth_smallest_matrix_with_validation(matrix, k):
    if not matrix or not matrix[0] or k <= 0:
        return None
    
    if k > len(matrix) * len(matrix[0]):
        return None
    
    import heapq
    heap = []
    
    for row in matrix:
        for num in row:
            heapq.heappush(heap, num)
    
    for _ in range(k - 1):
        heapq.heappop(heap)
    
    return heap[0]

def kth_smallest_matrix_with_constraints(matrix, k, constraints):
    import heapq
    heap = []
    
    for row in matrix:
        for num in row:
            if constraints(num):
                heapq.heappush(heap, num)
    
    if len(heap) < k:
        return None
    
    for _ in range(k - 1):
        heapq.heappop(heap)
    
    return heap[0]

def kth_smallest_matrix_with_optimization(matrix, k):
    import heapq
    heap = []
    
    for row in matrix:
        for num in row:
            heapq.heappush(heap, num)
    
    for _ in range(k - 1):
        heapq.heappop(heap)
    
    return heap[0]

def kth_smallest_matrix_with_advanced_optimization(matrix, k):
    import heapq
    heap = []
    
    for row in matrix:
        for num in row:
            heapq.heappush(heap, num)
    
    for _ in range(k - 1):
        heapq.heappop(heap)
    
    return heap[0]

def kth_smallest_matrix_with_count(matrix, k):
    import heapq
    heap = []
    count = 0
    
    for row in matrix:
        for num in row:
            heapq.heappush(heap, num)
            count += 1
    
    for _ in range(k - 1):
        heapq.heappop(heap)
    
    return heap[0], count

def kth_smallest_matrix_with_multiple(matrix, k):
    import heapq
    heap = []
    
    for row in matrix:
        for num in row:
            heapq.heappush(heap, num)
    
    for _ in range(k - 1):
        heapq.heappop(heap)
    
    return heap[0]

def kth_smallest_matrix_with_negative(matrix, k):
    import heapq
    heap = []
    
    for row in matrix:
        for num in row:
            heapq.heappush(heap, num)
    
    for _ in range(k - 1):
        heapq.heappop(heap)
    
    return heap[0]

def kth_smallest_matrix_with_circular(matrix, k):
    import heapq
    heap = []
    
    for i in range(2 * len(matrix)):
        row = matrix[i % len(matrix)]
        for num in row:
            heapq.heappush(heap, num)
    
    for _ in range(k - 1):
        heapq.heappop(heap)
    
    return heap[0]

def kth_smallest_matrix_with_validation_enhanced(matrix, k):
    if not matrix or not matrix[0] or k <= 0:
        return None
    
    if k > len(matrix) * len(matrix[0]):
        return None
    
    if k == 1:
        return min(min(row) for row in matrix)
    
    if k == len(matrix) * len(matrix[0]):
        return max(max(row) for row in matrix)
    
    import heapq
    heap = []
    
    for row in matrix:
        for num in row:
            heapq.heappush(heap, num)
    
    for _ in range(k - 1):
        heapq.heappop(heap)
    
    return heap[0]

def kth_smallest_matrix_with_optimization_enhanced(matrix, k):
    import heapq
    heap = []
    
    for row in matrix:
        for num in row:
            heapq.heappush(heap, num)
    
    for _ in range(k - 1):
        heapq.heappop(heap)
    
    return heap[0]

def kth_smallest_matrix_with_advanced_optimization_enhanced(matrix, k):
    import heapq
    heap = []
    
    for row in matrix:
        for num in row:
            heapq.heappush(heap, num)
    
    for _ in range(k - 1):
        heapq.heappop(heap)
    
    return heap[0]

def kth_smallest_matrix_with_statistics(matrix, k):
    import heapq
    heap = []
    count = 0
    sum_nums = 0
    
    for row in matrix:
        for num in row:
            heapq.heappush(heap, num)
            count += 1
            sum_nums += num
    
    for _ in range(k - 1):
        heapq.heappop(heap)
    
    return heap[0], {
        'count': count,
        'sum': sum_nums,
        'k': k
    }

def kth_smallest_matrix_with_advanced_features(matrix, k):
    import heapq
    heap = []
    count = 0
    sum_nums = 0
    min_val = float('inf')
    max_val = float('-inf')
    
    for row in matrix:
        for num in row:
            heapq.heappush(heap, num)
            count += 1
            sum_nums += num
            min_val = min(min_val, num)
            max_val = max(max_val, num)
    
    for _ in range(k - 1):
        heapq.heappop(heap)
    
    return heap[0], {
        'count': count,
        'sum': sum_nums,
        'k': k,
        'min': min_val,
        'max': max_val
    }

matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = 8

kth1 = kth_smallest_matrix_brute_force(matrix, k)
kth2 = kth_smallest_matrix_heap(matrix, k)
kth3 = kth_smallest_matrix_binary_search(matrix, k)
kth4 = kth_smallest_matrix_optimized(matrix, k)
kth5 = kth_smallest_matrix_with_validation(matrix, k)
kth6 = kth_smallest_matrix_with_optimization(matrix, k)
kth7 = kth_smallest_matrix_with_advanced_optimization(matrix, k)
kth8, count = kth_smallest_matrix_with_count(matrix, k)
kth9 = kth_smallest_matrix_with_multiple(matrix, k)
kth10 = kth_smallest_matrix_with_negative(matrix, k)
kth11 = kth_smallest_matrix_with_circular(matrix, k)
kth12 = kth_smallest_matrix_with_validation_enhanced(matrix, k)
kth13 = kth_smallest_matrix_with_optimization_enhanced(matrix, k)
kth14 = kth_smallest_matrix_with_advanced_optimization_enhanced(matrix, k)
kth15, stats = kth_smallest_matrix_with_statistics(matrix, k)
kth16, features = kth_smallest_matrix_with_advanced_features(matrix, k)

print(f"Matrix: {matrix}")
print(f"K: {k}")
print(f"Kth smallest (brute force): {kth1}")
print(f"Kth smallest (heap): {kth2}")
print(f"Kth smallest (binary search): {kth3}")
print(f"Kth smallest (optimized): {kth4}")
print(f"Kth smallest (with validation): {kth5}")
print(f"Kth smallest (with optimization): {kth6}")
print(f"Kth smallest (advanced optimization): {kth7}")
print(f"Kth smallest (with count): {kth8}, Count: {count}")
print(f"Kth smallest (with multiple): {kth9}")
print(f"Kth smallest (with negative): {kth10}")
print(f"Kth smallest (with circular): {kth11}")
print(f"Kth smallest (validation enhanced): {kth12}")
print(f"Kth smallest (optimization enhanced): {kth13}")
print(f"Kth smallest (advanced optimization enhanced): {kth14}")
print(f"Kth smallest (with statistics): {kth15}, Statistics: {stats}")
print(f"Kth smallest (with advanced features): {kth16}, Features: {features}")
