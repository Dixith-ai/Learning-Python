def max_product_subarray_brute_force(nums):
    max_product = float('-inf')
    
    for i in range(len(nums)):
        current_product = 1
        for j in range(i, len(nums)):
            current_product *= nums[j]
            max_product = max(max_product, current_product)
    
    return max_product

def max_product_subarray_dp(nums):
    if not nums:
        return 0
    
    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]
    
    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_product, min_product = min_product, max_product
        
        max_product = max(nums[i], max_product * nums[i]])
        min_product = min(nums[i], min_product * nums[i])
        
        result = max(result, max_product)
    
    return result

def max_product_subarray_optimized(nums):
    if not nums:
        return 0
    
    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]
    
    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_product, min_product = min_product, max_product
        
        max_product = max(nums[i], max_product * nums[i])
        min_product = min(nums[i], min_product * nums[i])
        
        result = max(result, max_product)
    
    return result

def max_product_subarray_with_validation(nums):
    if not nums:
        return 0
    
    if len(nums) == 1:
        return nums[0]
    
    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]
    
    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_product, min_product = min_product, max_product
        
        max_product = max(nums[i], max_product * nums[i])
        min_product = min(nums[i], min_product * nums[i])
        
        result = max(result, max_product)
    
    return result

def max_product_subarray_with_constraints(nums, constraints):
    if not nums:
        return 0
    
    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]
    
    for i in range(1, len(nums)):
        if not constraints(nums[i]):
            continue
        
        if nums[i] < 0:
            max_product, min_product = min_product, max_product
        
        max_product = max(nums[i], max_product * nums[i])
        min_product = min(nums[i], min_product * nums[i])
        
        result = max(result, max_product)
    
    return result

def max_product_subarray_with_optimization(nums):
    if not nums:
        return 0
    
    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]
    
    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_product, min_product = min_product, max_product
        
        max_product = max(nums[i], max_product * nums[i])
        min_product = min(nums[i], min_product * nums[i])
        
        result = max(result, max_product)
    
    return result

def max_product_subarray_with_advanced_optimization(nums):
    if not nums:
        return 0
    
    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]
    
    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_product, min_product = min_product, max_product
        
        max_product = max(nums[i], max_product * nums[i])
        min_product = min(nums[i], min_product * nums[i])
        
        result = max(result, max_product)
    
    return result

def max_product_subarray_with_count(nums):
    if not nums:
        return 0, 0
    
    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]
    count = 1
    
    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_product, min_product = min_product, max_product
        
        max_product = max(nums[i], max_product * nums[i])
        min_product = min(nums[i], min_product * nums[i])
        
        if max_product > result:
            result = max_product
            count = 1
        elif max_product == result:
            count += 1
    
    return result, count

def max_product_subarray_with_subarrays(nums):
    if not nums:
        return 0, []
    
    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]
    subarrays = [[nums[0]]]
    
    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_product, min_product = min_product, max_product
        
        max_product = max(nums[i], max_product * nums[i])
        min_product = min(nums[i], min_product * nums[i])
        
        if max_product > result:
            result = max_product
            subarrays = [[nums[i]]]
        elif max_product == result:
            subarrays.append([nums[i]])
    
    return result, subarrays

def max_product_subarray_with_negative(nums):
    if not nums:
        return 0
    
    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]
    
    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_product, min_product = min_product, max_product
        
        max_product = max(nums[i], max_product * nums[i])
        min_product = min(nums[i], min_product * nums[i])
        
        result = max(result, max_product)
    
    return result

def max_product_subarray_with_circular(nums):
    if not nums:
        return 0
    
    n = len(nums)
    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]
    
    for i in range(1, 2 * n):
        if nums[i % n] < 0:
            max_product, min_product = min_product, max_product
        
        max_product = max(nums[i % n], max_product * nums[i % n])
        min_product = min(nums[i % n], min_product * nums[i % n])
        
        result = max(result, max_product)
    
    return result

def max_product_subarray_with_validation_enhanced(nums):
    if not nums:
        return 0
    
    if len(nums) == 1:
        return nums[0]
    
    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]
    
    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_product, min_product = min_product, max_product
        
        max_product = max(nums[i], max_product * nums[i])
        min_product = min(nums[i], min_product * nums[i])
        
        result = max(result, max_product)
    
    return result

def max_product_subarray_with_optimization_enhanced(nums):
    if not nums:
        return 0
    
    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]
    
    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_product, min_product = min_product, max_product
        
        max_product = max(nums[i], max_product * nums[i])
        min_product = min(nums[i], min_product * nums[i])
        
        result = max(result, max_product)
    
    return result

def max_product_subarray_with_advanced_optimization_enhanced(nums):
    if not nums:
        return 0
    
    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]
    
    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_product, min_product = min_product, max_product
        
        max_product = max(nums[i], max_product * nums[i])
        min_product = min(nums[i], min_product * nums[i])
        
        result = max(result, max_product)
    
    return result

nums = [2, 3, -2, 4]

product1 = max_product_subarray_brute_force(nums)
product2 = max_product_subarray_dp(nums)
product3 = max_product_subarray_optimized(nums)
product4 = max_product_subarray_with_validation(nums)
product5 = max_product_subarray_with_optimization(nums)
product6 = max_product_subarray_with_advanced_optimization(nums)
product7, count = max_product_subarray_with_count(nums)
product8, subarrays = max_product_subarray_with_subarrays(nums)
product9 = max_product_subarray_with_negative(nums)
product10 = max_product_subarray_with_circular(nums)
product11 = max_product_subarray_with_validation_enhanced(nums)
product12 = max_product_subarray_with_optimization_enhanced(nums)
product13 = max_product_subarray_with_advanced_optimization_enhanced(nums)

print(f"Array: {nums}")
print(f"Max product (brute force): {product1}")
print(f"Max product (DP): {product2}")
print(f"Max product (optimized): {product3}")
print(f"Max product (with validation): {product4}")
print(f"Max product (with optimization): {product5}")
print(f"Max product (advanced optimization): {product6}")
print(f"Max product (with count): {product7}, Count: {count}")
print(f"Max product (with subarrays): {product8}, Subarrays: {subarrays}")
print(f"Max product (with negative): {product9}")
print(f"Max product (with circular): {product10}")
print(f"Max product (validation enhanced): {product11}")
print(f"Max product (optimization enhanced): {product12}")
print(f"Max product (advanced optimization enhanced): {product13}")
