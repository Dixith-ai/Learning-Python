def sum_natural_numbers(n):
    return n * (n + 1) // 2

def sum_natural_numbers_loop(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

n = 10
formula_result = sum_natural_numbers(n)
loop_result = sum_natural_numbers_loop(n)
print(f"Sum of first {n} natural numbers (formula): {formula_result}")
print(f"Sum of first {n} natural numbers (loop): {loop_result}")
