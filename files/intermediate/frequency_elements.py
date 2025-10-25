def count_frequency(lst):
    frequency = {}
    for item in lst:
        frequency[item] = frequency.get(item, 0) + 1
    return frequency

def count_frequency_counter(lst):
    from collections import Counter
    return dict(Counter(lst))

def count_frequency_defaultdict(lst):
    from collections import defaultdict
    frequency = defaultdict(int)
    for item in lst:
        frequency[item] += 1
    return dict(frequency)

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

freq1 = count_frequency(numbers)
freq2 = count_frequency_counter(numbers)
freq3 = count_frequency_defaultdict(numbers)

print(f"List: {numbers}")
print(f"Frequency: {freq1}")
print(f"Frequency (Counter): {freq2}")
print(f"Frequency (defaultdict): {freq3}")
