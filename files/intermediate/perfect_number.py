def is_perfect_number(number):
    if number <= 0:
        return False
    
    divisors = []
    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)
    
    return sum(divisors) == number

def is_perfect_number_optimized(number):
    if number <= 0:
        return False
    
    total = 1
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            total += i
            if i != number // i:
                total += number // i
    
    return total == number

def find_perfect_numbers(limit):
    perfect_numbers = []
    for i in range(1, limit + 1):
        if is_perfect_number_optimized(i):
            perfect_numbers.append(i)
    return perfect_numbers

number = 28
is_perfect = is_perfect_number(number)
is_perfect_opt = is_perfect_number_optimized(number)
perfect_nums = find_perfect_numbers(100)

print(f"Number: {number}")
print(f"Is perfect: {is_perfect}")
print(f"Is perfect (optimized): {is_perfect_opt}")
print(f"Perfect numbers up to 100: {perfect_nums}")
