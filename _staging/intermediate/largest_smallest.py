def find_largest_smallest(lst):
    if not lst:
        return None, None
    
    largest = smallest = lst[0]
    
    for num in lst:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    
    return largest, smallest

numbers = [3, 7, 2, 9, 1, 5, 8]
largest, smallest = find_largest_smallest(numbers)
print(f"List: {numbers}")
print(f"Largest: {largest}")
print(f"Smallest: {smallest}")
