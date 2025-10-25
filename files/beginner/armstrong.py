def is_armstrong(number):
    original_number = number
    num_digits = len(str(number))
    sum_of_powers = 0
    
    while number > 0:
        digit = number % 10
        sum_of_powers += digit ** num_digits
        number //= 10
    
    return sum_of_powers == original_number

number = 153
if is_armstrong(number):
    print(f"{number} is an Armstrong number")
else:
    print(f"{number} is not an Armstrong number")
