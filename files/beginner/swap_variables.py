a = 10
b = 20

print(f"Before swap: a = {a}, b = {b}")

a = a + b
b = a - b
a = a - b

print(f"After swap: a = {a}, b = {b}")

x = 5
y = 15
print(f"Before swap: x = {x}, y = {y}")

x, y = y, x

print(f"After swap: x = {x}, y = {y}")
