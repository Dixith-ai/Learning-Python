def is_symmetric(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    if rows != cols:
        return False
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != matrix[j][i]:
                return False
    
    return True

def is_skew_symmetric(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    if rows != cols:
        return False
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != -matrix[j][i]:
                return False
    
    return True

symmetric_matrix = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]
non_symmetric_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(f"Symmetric matrix: {symmetric_matrix}")
print(f"Is symmetric: {is_symmetric(symmetric_matrix)}")

print(f"Non-symmetric matrix: {non_symmetric_matrix}")
print(f"Is symmetric: {is_symmetric(non_symmetric_matrix)}")
