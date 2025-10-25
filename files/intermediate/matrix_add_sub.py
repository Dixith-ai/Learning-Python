def matrix_add(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    
    return result

def matrix_subtract(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] - matrix2[i][j]
    
    return result

matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

addition = matrix_add(matrix1, matrix2)
subtraction = matrix_subtract(matrix1, matrix2)

print(f"Matrix 1: {matrix1}")
print(f"Matrix 2: {matrix2}")
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
