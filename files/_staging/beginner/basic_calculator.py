def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

a = 10
b = 5
print(f"Addition: {add(a, b)}")
print(f"Subtraction: {subtract(a, b)}")
print(f"Multiplication: {multiply(a, b)}")
print(f"Division: {divide(a, b)}")
