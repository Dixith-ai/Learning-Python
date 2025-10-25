def sum_of_digits(number):
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number //= 10
    return total

number = 12345
digit_sum = sum_of_digits(number)
print(f"Sum of digits in {number}: {digit_sum}")
