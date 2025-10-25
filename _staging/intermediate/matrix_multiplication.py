def matrix_multiply(matrix1, matrix2):
    rows1, cols1 = len(matrix1), len(matrix1[0])
    rows2, cols2 = len(matrix2), len(matrix2[0])
    
    if cols1 != rows2:
        return None
    
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]
    
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result

matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

result = matrix_multiply(matrix1, matrix2)
print(f"Matrix 1: {matrix1}")
print(f"Matrix 2: {matrix2}")
print(f"Result: {result}")
