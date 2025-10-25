def n_queens_recursive(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                return False
        return True
    
    def solve(board, row):
        if row == n:
            return [board[:]]
        
        solutions = []
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solutions.extend(solve(board, row + 1))
        return solutions
    
    board = [-1] * n
    return solve(board, 0)

def n_queens_backtracking(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                return False
        return True
    
    def backtrack(board, row):
        if row == n:
            result.append(board[:])
            return
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(board, row + 1)
                board[row] = -1
    
    result = []
    board = [-1] * n
    backtrack(board, 0)
    return result

def n_queens_iterative(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                return False
        return True
    
    solutions = []
    stack = [(0, [-1] * n)]
    
    while stack:
        row, board = stack.pop()
        
        if row == n:
            solutions.append(board[:])
            continue
        
        for col in range(n):
            if is_safe(board, row, col):
                new_board = board[:]
                new_board[row] = col
                stack.append((row + 1, new_board))
    
    return solutions

def n_queens_with_constraints(n, constraints):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                return False
        
        for constraint in constraints:
            if not constraint(board, row, col):
                return False
        
        return True
    
    def backtrack(board, row):
        if row == n:
            result.append(board[:])
            return
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(board, row + 1)
                board[row] = -1
    
    result = []
    board = [-1] * n
    backtrack(board, 0)
    return result

def n_queens_with_validation(n):
    if n <= 0:
        return []
    
    if n == 1:
        return [[0]]
    
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                return False
        return True
    
    def backtrack(board, row):
        if row == n:
            result.append(board[:])
            return
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(board, row + 1)
                board[row] = -1
    
    result = []
    board = [-1] * n
    backtrack(board, 0)
    return result

def n_queens_with_optimization(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                return False
        return True
    
    def backtrack(board, row):
        if row == n:
            result.append(board[:])
            return
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(board, row + 1)
                board[row] = -1
    
    result = []
    board = [-1] * n
    backtrack(board, 0)
    return result

def n_queens_with_count(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                return False
        return True
    
    def backtrack(board, row):
        if row == n:
            return 1
        
        count = 0
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                count += backtrack(board, row + 1)
                board[row] = -1
        
        return count
    
    board = [-1] * n
    return backtrack(board, 0)

def n_queens_with_visualization(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                return False
        return True
    
    def backtrack(board, row):
        if row == n:
            result.append(board[:])
            return
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(board, row + 1)
                board[row] = -1
    
    result = []
    board = [-1] * n
    backtrack(board, 0)
    
    def visualize_solution(solution):
        board = [['.' for _ in range(n)] for _ in range(n)]
        for row, col in enumerate(solution):
            board[row][col] = 'Q'
        return board
    
    return result, [visualize_solution(sol) for sol in result]

def n_queens_with_optimization_advanced(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                return False
        return True
    
    def backtrack(board, row):
        if row == n:
            result.append(board[:])
            return
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(board, row + 1)
                board[row] = -1
    
    result = []
    board = [-1] * n
    backtrack(board, 0)
    return result

n = 4

queens1 = n_queens_recursive(n)
queens2 = n_queens_backtracking(n)
queens3 = n_queens_iterative(n)
queens4 = n_queens_with_validation(n)
queens5 = n_queens_with_optimization(n)
queens6 = n_queens_with_count(n)
queens7, visualizations = n_queens_with_visualization(n)
queens8 = n_queens_with_optimization_advanced(n)

print(f"N-Queens for n={n}:")
print(f"Solutions (recursive): {queens1}")
print(f"Solutions (backtracking): {queens2}")
print(f"Solutions (iterative): {queens3}")
print(f"Solutions (with validation): {queens4}")
print(f"Solutions (with optimization): {queens5}")
print(f"Number of solutions: {queens6}")
print(f"Solutions (with visualization): {queens7}")
print(f"Solutions (advanced optimization): {queens8}")

for i, viz in enumerate(visualizations):
    print(f"Solution {i+1}:")
    for row in viz:
        print(' '.join(row))
    print()
