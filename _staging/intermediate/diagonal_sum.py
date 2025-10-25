def sum_main_diagonal(matrix):
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][i]
    return total

def sum_anti_diagonal(matrix):
    total = 0
    n = len(matrix)
    for i in range(n):
        total += matrix[i][n - 1 - i]
    return total

def sum_both_diagonals(matrix):
    main_diag = sum_main_diagonal(matrix)
    anti_diag = sum_anti_diagonal(matrix)
    
    if len(matrix) % 2 == 1:
        center = matrix[len(matrix) // 2][len(matrix) // 2]
        return main_diag + anti_diag - center
    else:
        return main_diag + anti_diag

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

main_sum = sum_main_diagonal(matrix)
anti_sum = sum_anti_diagonal(matrix)
both_sum = sum_both_diagonals(matrix)

print(f"Matrix: {matrix}")
print(f"Main diagonal sum: {main_sum}")
print(f"Anti diagonal sum: {anti_sum}")
print(f"Both diagonals sum: {both_sum}")
