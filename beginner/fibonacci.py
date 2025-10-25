def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_series(n):
    series = []
    for i in range(n):
        series.append(fibonacci_iterative(i))
    return series

n = 10
print(f"Fibonacci series of {n} numbers: {fibonacci_series(n)}")
print(f"Fibonacci({n}) iterative: {fibonacci_iterative(n)}")
print(f"Fibonacci({n}) recursive: {fibonacci_recursive(n)}")
