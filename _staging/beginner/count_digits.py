def count_digits(number):
    count = 0
    while number > 0:
        count += 1
        number //= 10
    return count

number = 12345
digit_count = count_digits(number)
print(f"Number of digits in {number}: {digit_count}")
