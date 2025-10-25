def is_power_of_two_builtin(n):
    return n > 0 and bin(n).count('1') == 1

def is_power_of_two_bitwise(n):
    return n > 0 and (n & (n - 1)) == 0

def is_power_of_two_loop(n):
    if n <= 0:
        return False
    
    while n > 1:
        if n % 2 != 0:
            return False
        n //= 2
    
    return True

def is_power_of_two_log(n):
    import math
    if n <= 0:
        return False
    return math.log2(n).is_integer()

def get_next_power_of_two(n):
    if n <= 0:
        return 1
    
    power = 1
    while power < n:
        power <<= 1
    return power

def get_previous_power_of_two(n):
    if n <= 0:
        return 0
    
    power = 1
    while power < n:
        power <<= 1
    return power >> 1

numbers = [1, 2, 3, 4, 8, 16, 32, 33]

for num in numbers:
    power1 = is_power_of_two_builtin(num)
    power2 = is_power_of_two_bitwise(num)
    power3 = is_power_of_two_loop(num)
    power4 = is_power_of_two_log(num)
    
    print(f"{num}: {power1} {power2} {power3} {power4}")

print(f"Next power of 2 for 5: {get_next_power_of_two(5)}")
print(f"Previous power of 2 for 5: {get_previous_power_of_two(5)}")
