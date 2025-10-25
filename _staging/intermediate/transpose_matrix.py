def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    
    return transposed

def transpose_matrix_zip(matrix):
    return list(map(list, zip(*matrix)))

matrix = [[1, 2, 3], [4, 5, 6]]

transposed = transpose_matrix(matrix)
transposed_zip = transpose_matrix_zip(matrix)

print(f"Original: {matrix}")
print(f"Transposed: {transposed}")
print(f"Transposed (zip): {transposed_zip}")
