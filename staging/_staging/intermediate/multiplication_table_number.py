def print_multiplication_table_of_number(number, limit):
    print(f"Multiplication table of {number}:")
    for i in range(1, limit + 1):
        print(f"{number} x {i} = {number * i}")

number = 7
limit = 10
print_multiplication_table_of_number(number, limit)
