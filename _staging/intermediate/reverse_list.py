def reverse_list_slicing(lst):
    return lst[::-1]

def reverse_list_loop(lst):
    result = []
    for i in range(len(lst) - 1, -1, -1):
        result.append(lst[i])
    return result

def reverse_list_inplace(lst):
    left = 0
    right = len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst

numbers = [1, 2, 3, 4, 5]
print(f"Original: {numbers}")

reversed_slicing = reverse_list_slicing(numbers)
reversed_loop = reverse_list_loop(numbers)
reversed_inplace = reverse_list_inplace(numbers.copy())

print(f"Reversed (slicing): {reversed_slicing}")
print(f"Reversed (loop): {reversed_loop}")
print(f"Reversed (in-place): {reversed_inplace}")
