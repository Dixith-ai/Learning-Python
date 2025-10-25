def majority_element_boyer_moore(nums):
    candidate = None
    count = 0
    
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    
    return candidate

def majority_element_boyer_moore_with_validation(nums):
    if not nums:
        return None
    
    candidate = None
    count = 0
    
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    
    count = 0
    for num in nums:
        if num == candidate:
            count += 1
    
    return candidate if count > len(nums) // 2 else None

def majority_element_boyer_moore_with_count(nums):
    candidate = None
    count = 0
    
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    
    actual_count = 0
    for num in nums:
        if num == candidate:
            actual_count += 1
    
    return candidate, actual_count

def majority_element_boyer_moore_with_optimization(nums):
    candidate = None
    count = 0
    
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    
    return candidate

def majority_element_boyer_moore_with_advanced_optimization(nums):
    candidate = None
    count = 0
    
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    
    return candidate

def majority_element_boyer_moore_with_constraints(nums, constraints):
    candidate = None
    count = 0
    
    for num in nums:
        if constraints(num):
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
    
    return candidate

def majority_element_boyer_moore_with_validation_enhanced(nums):
    if not nums:
        return None
    
    if len(nums) == 1:
        return nums[0]
    
    candidate = None
    count = 0
    
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    
    count = 0
    for num in nums:
        if num == candidate:
            count += 1
    
    return candidate if count > len(nums) // 2 else None

def majority_element_boyer_moore_with_multiple_candidates(nums):
    candidate1 = None
    candidate2 = None
    count1 = 0
    count2 = 0
    
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1 = num
            count1 = 1
        elif count2 == 0:
            candidate2 = num
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1
    
    count1 = count2 = 0
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
    
    result = []
    if count1 > len(nums) // 3:
        result.append(candidate1)
    if count2 > len(nums) // 3:
        result.append(candidate2)
    
    return result

def majority_element_boyer_moore_with_optimization_enhanced(nums):
    candidate = None
    count = 0
    
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    
    return candidate

def majority_element_boyer_moore_with_advanced_optimization(nums):
    candidate = None
    count = 0
    
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    
    return candidate

nums = [3, 2, 3]

majority1 = majority_element_boyer_moore(nums)
majority2 = majority_element_boyer_moore_with_validation(nums)
majority3, count = majority_element_boyer_moore_with_count(nums)
majority4 = majority_element_boyer_moore_with_optimization(nums)
majority5 = majority_element_boyer_moore_with_advanced_optimization(nums)
majority6 = majority_element_boyer_moore_with_validation_enhanced(nums)
majority7 = majority_element_boyer_moore_with_multiple_candidates(nums)
majority8 = majority_element_boyer_moore_with_optimization_enhanced(nums)
majority9 = majority_element_boyer_moore_with_advanced_optimization(nums)

print(f"Array: {nums}")
print(f"Majority element (Boyer-Moore): {majority1}")
print(f"Majority element (with validation): {majority2}")
print(f"Majority element (with count): {majority3}, Count: {count}")
print(f"Majority element (with optimization): {majority4}")
print(f"Majority element (advanced optimization): {majority5}")
print(f"Majority element (validation enhanced): {majority6}")
print(f"Majority element (multiple candidates): {majority7}")
print(f"Majority element (optimization enhanced): {majority8}")
print(f"Majority element (advanced optimization): {majority9}")
