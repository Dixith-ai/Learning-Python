def find_missing_number_xor(nums):
    n = len(nums)
    xor_all = 0
    xor_nums = 0
    
    for i in range(1, n + 2):
        xor_all ^= i
    
    for num in nums:
        xor_nums ^= num
    
    return xor_all ^ xor_nums

def find_missing_number_sum(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

def find_missing_number_sort(nums):
    nums.sort()
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return i + 1
    return len(nums) + 1

def find_missing_number_hashset(nums):
    num_set = set(nums)
    for i in range(1, len(nums) + 2):
        if i not in num_set:
            return i
    return len(nums) + 1

def find_missing_number_optimized(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

def find_missing_number_with_validation(nums):
    if not nums:
        return 1
    
    if len(nums) == 1:
        return 2 if nums[0] == 1 else 1
    
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

def find_missing_number_with_constraints(nums, constraints):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = 0
    
    for num in nums:
        if constraints(num):
            actual_sum += num
    
    return expected_sum - actual_sum

def find_missing_number_with_optimization(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

def find_missing_number_with_advanced_optimization(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

def find_missing_number_with_count(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    missing = expected_sum - actual_sum
    return missing, 1

def find_missing_number_with_multiple(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    missing = expected_sum - actual_sum
    
    if missing > n + 1:
        return []
    
    return [missing]

def find_missing_number_with_negative(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

def find_missing_number_with_circular(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

def find_missing_number_with_validation_enhanced(nums):
    if not nums:
        return 1
    
    if len(nums) == 1:
        return 2 if nums[0] == 1 else 1
    
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

def find_missing_number_with_optimization_enhanced(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

def find_missing_number_with_advanced_optimization_enhanced(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

def find_missing_number_with_statistics(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    missing = expected_sum - actual_sum
    
    return missing, {
        'expected_sum': expected_sum,
        'actual_sum': actual_sum,
        'difference': missing,
        'count': len(nums)
    }

def find_missing_number_with_advanced_features(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    missing = expected_sum - actual_sum
    
    return missing, {
        'expected_sum': expected_sum,
        'actual_sum': actual_sum,
        'difference': missing,
        'count': len(nums),
        'min': min(nums) if nums else 0,
        'max': max(nums) if nums else 0
    }

nums = [1, 2, 4, 5]

missing1 = find_missing_number_xor(nums)
missing2 = find_missing_number_sum(nums)
missing3 = find_missing_number_sort(nums)
missing4 = find_missing_number_hashset(nums)
missing5 = find_missing_number_optimized(nums)
missing6 = find_missing_number_with_validation(nums)
missing7 = find_missing_number_with_optimization(nums)
missing8 = find_missing_number_with_advanced_optimization(nums)
missing9, count = find_missing_number_with_count(nums)
missing10 = find_missing_number_with_multiple(nums)
missing11 = find_missing_number_with_negative(nums)
missing12 = find_missing_number_with_circular(nums)
missing13 = find_missing_number_with_validation_enhanced(nums)
missing14 = find_missing_number_with_optimization_enhanced(nums)
missing15 = find_missing_number_with_advanced_optimization_enhanced(nums)
missing16, stats = find_missing_number_with_statistics(nums)
missing17, features = find_missing_number_with_advanced_features(nums)

print(f"Array: {nums}")
print(f"Missing number (XOR): {missing1}")
print(f"Missing number (sum): {missing2}")
print(f"Missing number (sort): {missing3}")
print(f"Missing number (hashset): {missing4}")
print(f"Missing number (optimized): {missing5}")
print(f"Missing number (with validation): {missing6}")
print(f"Missing number (with optimization): {missing7}")
print(f"Missing number (advanced optimization): {missing8}")
print(f"Missing number (with count): {missing9}, Count: {count}")
print(f"Missing number (with multiple): {missing10}")
print(f"Missing number (with negative): {missing11}")
print(f"Missing number (with circular): {missing12}")
print(f"Missing number (validation enhanced): {missing13}")
print(f"Missing number (optimization enhanced): {missing14}")
print(f"Missing number (advanced optimization enhanced): {missing15}")
print(f"Missing number (with statistics): {missing16}, Statistics: {stats}")
print(f"Missing number (with advanced features): {missing17}, Features: {features}")
