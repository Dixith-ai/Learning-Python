def find_second_largest(lst):
    if len(lst) < 2:
        return None
    
    largest = second_largest = float('-inf')
    
    for num in lst:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    return second_largest if second_largest != float('-inf') else None

def find_second_largest_sorted(lst):
    if len(lst) < 2:
        return None
    
    unique_sorted = sorted(set(lst), reverse=True)
    return unique_sorted[1] if len(unique_sorted) > 1 else None

numbers = [3, 7, 2, 9, 1, 5, 8, 9]
second_largest = find_second_largest(numbers)
second_largest_sorted = find_second_largest_sorted(numbers)

print(f"List: {numbers}")
print(f"Second largest: {second_largest}")
print(f"Second largest (sorted): {second_largest_sorted}")
