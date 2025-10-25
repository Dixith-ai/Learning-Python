def longest_consecutive_sequence_set(nums):
    if not nums:
        return 0
    
    num_set = set(nums)
    max_length = 0
    
    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            
            max_length = max(max_length, current_length)
    
    return max_length

def longest_consecutive_sequence_sort(nums):
    if not nums:
        return 0
    
    nums.sort()
    max_length = 1
    current_length = 1
    
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            current_length += 1
        elif nums[i] != nums[i - 1]:
            max_length = max(max_length, current_length)
            current_length = 1
    
    return max(max_length, current_length)

def longest_consecutive_sequence_dict(nums):
    if not nums:
        return 0
    
    num_dict = {}
    max_length = 0
    
    for num in nums:
        if num not in num_dict:
            left = num_dict.get(num - 1, 0)
            right = num_dict.get(num + 1, 0)
            
            current_length = left + right + 1
            max_length = max(max_length, current_length)
            
            num_dict[num] = current_length
            num_dict[num - left] = current_length
            num_dict[num + right] = current_length
    
    return max_length

def longest_consecutive_sequence_brute_force(nums):
    if not nums:
        return 0
    
    max_length = 0
    
    for num in nums:
        current_num = num
        current_length = 1
        
        while current_num + 1 in nums:
            current_num += 1
            current_length += 1
        
        max_length = max(max_length, current_length)
    
    return max_length

def longest_consecutive_sequence_with_sequence(nums):
    if not nums:
        return 0, []
    
    num_set = set(nums)
    max_length = 0
    longest_sequence = []
    
    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_sequence = [current_num]
            
            while current_num + 1 in num_set:
                current_num += 1
                current_sequence.append(current_num)
            
            if len(current_sequence) > max_length:
                max_length = len(current_sequence)
                longest_sequence = current_sequence
    
    return max_length, longest_sequence

def longest_consecutive_sequence_with_validation(nums):
    if not nums:
        return 0
    
    if len(nums) == 1:
        return 1
    
    num_set = set(nums)
    max_length = 0
    
    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            
            max_length = max(max_length, current_length)
    
    return max_length

def longest_consecutive_sequence_with_constraints(nums, constraints):
    if not nums:
        return 0
    
    num_set = set(nums)
    max_length = 0
    
    for num in num_set:
        if num - 1 not in num_set and constraints(num):
            current_num = num
            current_length = 1
            
            while current_num + 1 in num_set and constraints(current_num + 1):
                current_num += 1
                current_length += 1
            
            max_length = max(max_length, current_length)
    
    return max_length

def longest_consecutive_sequence_with_optimization(nums):
    if not nums:
        return 0
    
    num_set = set(nums)
    max_length = 0
    
    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            
            max_length = max(max_length, current_length)
    
    return max_length

def longest_consecutive_sequence_with_advanced_optimization(nums):
    if not nums:
        return 0
    
    num_set = set(nums)
    max_length = 0
    
    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            
            max_length = max(max_length, current_length)
    
    return max_length

def longest_consecutive_sequence_with_count(nums):
    if not nums:
        return 0
    
    num_set = set(nums)
    max_length = 0
    count = 0
    
    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            
            if current_length > max_length:
                max_length = current_length
                count = 1
            elif current_length == max_length:
                count += 1
    
    return max_length, count

nums = [100, 4, 200, 1, 3, 2]

sequence1 = longest_consecutive_sequence_set(nums)
sequence2 = longest_consecutive_sequence_sort(nums)
sequence3 = longest_consecutive_sequence_dict(nums)
sequence4 = longest_consecutive_sequence_brute_force(nums)
sequence5, longest_seq = longest_consecutive_sequence_with_sequence(nums)
sequence6 = longest_consecutive_sequence_with_validation(nums)
sequence7 = longest_consecutive_sequence_with_optimization(nums)
sequence8 = longest_consecutive_sequence_with_advanced_optimization(nums)
sequence9, count = longest_consecutive_sequence_with_count(nums)

print(f"Array: {nums}")
print(f"Longest consecutive sequence (set): {sequence1}")
print(f"Longest consecutive sequence (sort): {sequence2}")
print(f"Longest consecutive sequence (dict): {sequence3}")
print(f"Longest consecutive sequence (brute force): {sequence4}")
print(f"Longest consecutive sequence (with sequence): {sequence5}, Sequence: {longest_seq}")
print(f"Longest consecutive sequence (with validation): {sequence6}")
print(f"Longest consecutive sequence (with optimization): {sequence7}")
print(f"Longest consecutive sequence (advanced optimization): {sequence8}")
print(f"Longest consecutive sequence (with count): {sequence9}, Count: {count}")
