def print_multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i} x {j} = {i * j}", end="\t")
        print()

n = 5
print(f"Multiplication table from 1 to {n}:")
print_multiplication_table(n)
