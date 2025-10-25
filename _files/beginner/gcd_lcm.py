def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)

a = 48
b = 18

gcd_result = gcd(a, b)
lcm_result = lcm(a, b)
gcd_recursive_result = gcd_recursive(a, b)

print(f"GCD of {a} and {b}: {gcd_result}")
print(f"LCM of {a} and {b}: {lcm_result}")
print(f"GCD recursive of {a} and {b}: {gcd_recursive_result}")
