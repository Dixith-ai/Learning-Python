def solve_sudoku_recursive(board):
    def is_valid(board, row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        
        return True
    
    def solve(board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid(board, row, col, num):
                            board[row][col] = num
                            if solve(board):
                                return True
                            board[row][col] = 0
                    return False
        return True
    
    return solve(board)

def solve_sudoku_backtracking(board):
    def is_valid(board, row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        
        return True
    
    def backtrack(board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid(board, row, col, num):
                            board[row][col] = num
                            if backtrack(board):
                                return True
                            board[row][col] = 0
                    return False
        return True
    
    return backtrack(board)

def solve_sudoku_optimized(board):
    def is_valid(board, row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        
        return True
    
    def find_empty_cell(board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    return row, col
        return None, None
    
    def solve(board):
        row, col = find_empty_cell(board)
        if row is None:
            return True
        
        for num in range(1, 10):
            if is_valid(board, row, col, num):
                board[row][col] = num
                if solve(board):
                    return True
                board[row][col] = 0
        
        return False
    
    return solve(board)

def solve_sudoku_with_validation(board):
    def is_valid_board(board):
        for row in range(9):
            for col in range(9):
                if board[row][col] != 0:
                    if not is_valid_cell(board, row, col, board[row][col]):
                        return False
        return True
    
    def is_valid_cell(board, row, col, num):
        for i in range(9):
            if i != col and board[row][i] == num:
                return False
            if i != row and board[i][col] == num:
                return False
        
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if (i != row or j != col) and board[i][j] == num:
                    return False
        
        return True
    
    def solve(board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid_cell(board, row, col, num):
                            board[row][col] = num
                            if solve(board):
                                return True
                            board[row][col] = 0
                    return False
        return True
    
    if not is_valid_board(board):
        return False
    
    return solve(board)

def solve_sudoku_with_constraints(board, constraints):
    def is_valid(board, row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        
        for constraint in constraints:
            if not constraint(board, row, col, num):
                return False
        
        return True
    
    def solve(board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid(board, row, col, num):
                            board[row][col] = num
                            if solve(board):
                                return True
                            board[row][col] = 0
                    return False
        return True
    
    return solve(board)

def solve_sudoku_with_optimization(board):
    def is_valid(board, row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        
        return True
    
    def find_best_cell(board):
        min_options = 10
        best_row, best_col = -1, -1
        
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    options = 0
                    for num in range(1, 10):
                        if is_valid(board, row, col, num):
                            options += 1
                    
                    if options < min_options:
                        min_options = options
                        best_row, best_col = row, col
        
        return best_row, best_col
    
    def solve(board):
        row, col = find_best_cell(board)
        if row == -1:
            return True
        
        for num in range(1, 10):
            if is_valid(board, row, col, num):
                board[row][col] = num
                if solve(board):
                    return True
                board[row][col] = 0
        
        return False
    
    return solve(board)

def solve_sudoku_with_count(board):
    count = 0
    
    def is_valid(board, row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        
        return True
    
    def solve(board):
        nonlocal count
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid(board, row, col, num):
                            board[row][col] = num
                            if solve(board):
                                count += 1
                            board[row][col] = 0
                    return False
        return True
    
    solve(board)
    return count

def solve_sudoku_with_visualization(board):
    def is_valid(board, row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        
        return True
    
    def solve(board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid(board, row, col, num):
                            board[row][col] = num
                            if solve(board):
                                return True
                            board[row][col] = 0
                    return False
        return True
    
    def print_board(board):
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - -")
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                print(board[i][j], end=" ")
            print()
    
    result = solve(board)
    if result:
        print_board(board)
    return result

def solve_sudoku_with_advanced_optimization(board):
    def is_valid(board, row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        
        return True
    
    def solve(board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid(board, row, col, num):
                            board[row][col] = num
                            if solve(board):
                                return True
                            board[row][col] = 0
                    return False
        return True
    
    return solve(board)

board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

board_copy1 = [row[:] for row in board]
board_copy2 = [row[:] for row in board]
board_copy3 = [row[:] for row in board]
board_copy4 = [row[:] for row in board]
board_copy5 = [row[:] for row in board]
board_copy6 = [row[:] for row in board]
board_copy7 = [row[:] for row in board]
board_copy8 = [row[:] for row in board]

sudoku1 = solve_sudoku_recursive(board_copy1)
sudoku2 = solve_sudoku_backtracking(board_copy2)
sudoku3 = solve_sudoku_optimized(board_copy3)
sudoku4 = solve_sudoku_with_validation(board_copy4)
sudoku5 = solve_sudoku_with_optimization(board_copy5)
sudoku6 = solve_sudoku_with_count(board_copy6)
sudoku7 = solve_sudoku_with_visualization(board_copy7)
sudoku8 = solve_sudoku_with_advanced_optimization(board_copy8)

print(f"Sudoku solved (recursive): {sudoku1}")
print(f"Sudoku solved (backtracking): {sudoku2}")
print(f"Sudoku solved (optimized): {sudoku3}")
print(f"Sudoku solved (with validation): {sudoku4}")
print(f"Sudoku solved (with optimization): {sudoku5}")
print(f"Sudoku solutions count: {sudoku6}")
print(f"Sudoku solved (with visualization): {sudoku7}")
print(f"Sudoku solved (advanced optimization): {sudoku8}")
