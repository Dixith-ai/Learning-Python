def hamming_weight_builtin(n):
    return bin(n).count('1')

def hamming_weight_manual(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

def hamming_weight_brian_kernighan(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count

def hamming_weight_lookup_table(n):
    table = [0] * 256
    for i in range(256):
        table[i] = (i & 1) + table[i >> 1]
    
    count = 0
    while n:
        count += table[n & 0xFF]
        n >>= 8
    return count

number = 11
weight1 = hamming_weight_builtin(number)
weight2 = hamming_weight_manual(number)
weight3 = hamming_weight_brian_kernighan(number)
weight4 = hamming_weight_lookup_table(number)

print(f"Number: {number} (binary: {bin(number)})")
print(f"Hamming weight (builtin): {weight1}")
print(f"Hamming weight (manual): {weight2}")
print(f"Hamming weight (Brian Kernighan): {weight3}")
print(f"Hamming weight (lookup table): {weight4}")
