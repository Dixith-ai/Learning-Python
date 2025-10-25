def count_paths_maze_recursive(maze, start, end):
    def helper(row, col):
        if row == end[0] and col == end[1]:
            return 1
        
        if row >= len(maze) or col >= len(maze[0]) or maze[row][col] == 1:
            return 0
        
        return helper(row + 1, col) + helper(row, col + 1)
    
    return helper(start[0], start[1])

def count_paths_maze_memoization(maze, start, end):
    memo = {}
    
    def helper(row, col):
        if (row, col) in memo:
            return memo[(row, col)]
        
        if row == end[0] and col == end[1]:
            return 1
        
        if row >= len(maze) or col >= len(maze[0]) or maze[row][col] == 1:
            return 0
        
        result = helper(row + 1, col) + helper(row, col + 1)
        memo[(row, col)] = result
        return result
    
    return helper(start[0], start[1])

def count_paths_maze_dp(maze, start, end):
    m, n = len(maze), len(maze[0])
    dp = [[0] * n for _ in range(m)]
    
    dp[start[0]][start[1]] = 1
    
    for i in range(start[0], m):
        for j in range(start[1], n):
            if maze[i][j] == 1:
                dp[i][j] = 0
            else:
                if i > start[0]:
                    dp[i][j] += dp[i - 1][j]
                if j > start[1]:
                    dp[i][j] += dp[i][j - 1]
    
    return dp[end[0]][end[1]]

def count_paths_maze_with_obstacles(maze, start, end):
    m, n = len(maze), len(maze[0])
    dp = [[0] * n for _ in range(m)]
    
    dp[start[0]][start[1]] = 1
    
    for i in range(start[0], m):
        for j in range(start[1], n):
            if maze[i][j] == 1:
                dp[i][j] = 0
            else:
                if i > start[0]:
                    dp[i][j] += dp[i - 1][j]
                if j > start[1]:
                    dp[i][j] += dp[i][j - 1]
    
    return dp[end[0]][end[1]]

def count_paths_maze_with_diagonal(maze, start, end):
    m, n = len(maze), len(maze[0])
    dp = [[0] * n for _ in range(m)]
    
    dp[start[0]][start[1]] = 1
    
    for i in range(start[0], m):
        for j in range(start[1], n):
            if maze[i][j] == 1:
                dp[i][j] = 0
            else:
                if i > start[0]:
                    dp[i][j] += dp[i - 1][j]
                if j > start[1]:
                    dp[i][j] += dp[i][j - 1]
                if i > start[0] and j > start[1]:
                    dp[i][j] += dp[i - 1][j - 1]
    
    return dp[end[0]][end[1]]

def count_paths_maze_with_constraints(maze, start, end, constraints):
    m, n = len(maze), len(maze[0])
    dp = [[0] * n for _ in range(m)]
    
    dp[start[0]][start[1]] = 1
    
    for i in range(start[0], m):
        for j in range(start[1], n):
            if maze[i][j] == 1 or not constraints(i, j):
                dp[i][j] = 0
            else:
                if i > start[0]:
                    dp[i][j] += dp[i - 1][j]
                if j > start[1]:
                    dp[i][j] += dp[i][j - 1]
    
    return dp[end[0]][end[1]]

def count_paths_maze_with_validation(maze, start, end):
    if not maze or not maze[0]:
        return 0
    
    if start[0] >= len(maze) or start[1] >= len(maze[0]):
        return 0
    
    if end[0] >= len(maze) or end[1] >= len(maze[0]):
        return 0
    
    m, n = len(maze), len(maze[0])
    dp = [[0] * n for _ in range(m)]
    
    dp[start[0]][start[1]] = 1
    
    for i in range(start[0], m):
        for j in range(start[1], n):
            if maze[i][j] == 1:
                dp[i][j] = 0
            else:
                if i > start[0]:
                    dp[i][j] += dp[i - 1][j]
                if j > start[1]:
                    dp[i][j] += dp[i][j - 1]
    
    return dp[end[0]][end[1]]

def count_paths_maze_with_optimization(maze, start, end):
    m, n = len(maze), len(maze[0])
    dp = [[0] * n for _ in range(m)]
    
    dp[start[0]][start[1]] = 1
    
    for i in range(start[0], m):
        for j in range(start[1], n):
            if maze[i][j] == 1:
                dp[i][j] = 0
            else:
                if i > start[0]:
                    dp[i][j] += dp[i - 1][j]
                if j > start[1]:
                    dp[i][j] += dp[i][j - 1]
    
    return dp[end[0]][end[1]]

def count_paths_maze_with_advanced_optimization(maze, start, end):
    m, n = len(maze), len(maze[0])
    dp = [[0] * n for _ in range(m)]
    
    dp[start[0]][start[1]] = 1
    
    for i in range(start[0], m):
        for j in range(start[1], n):
            if maze[i][j] == 1:
                dp[i][j] = 0
            else:
                if i > start[0]:
                    dp[i][j] += dp[i - 1][j]
                if j > start[1]:
                    dp[i][j] += dp[i][j - 1]
    
    return dp[end[0]][end[1]]

def count_paths_maze_with_paths(maze, start, end):
    m, n = len(maze), len(maze[0])
    dp = [[0] * n for _ in range(m)]
    
    dp[start[0]][start[1]] = 1
    
    for i in range(start[0], m):
        for j in range(start[1], n):
            if maze[i][j] == 1:
                dp[i][j] = 0
            else:
                if i > start[0]:
                    dp[i][j] += dp[i - 1][j]
                if j > start[1]:
                    dp[i][j] += dp[i][j - 1]
    
    def get_paths(row, col, path):
        if row == start[0] and col == start[1]:
            return [path]
        
        paths = []
        if row > start[0] and dp[row - 1][col] > 0:
            paths.extend(get_paths(row - 1, col, path + [(row, col)]))
        if col > start[1] and dp[row][col - 1] > 0:
            paths.extend(get_paths(row, col - 1, path + [(row, col)]))
        
        return paths
    
    return dp[end[0]][end[1]], get_paths(end[0], end[1], [])

maze = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
start = (0, 0)
end = (3, 3)

paths1 = count_paths_maze_recursive(maze, start, end)
paths2 = count_paths_maze_memoization(maze, start, end)
paths3 = count_paths_maze_dp(maze, start, end)
paths4 = count_paths_maze_with_obstacles(maze, start, end)
paths5 = count_paths_maze_with_diagonal(maze, start, end)
paths6 = count_paths_maze_with_validation(maze, start, end)
paths7 = count_paths_maze_with_optimization(maze, start, end)
paths8 = count_paths_maze_with_advanced_optimization(maze, start, end)
paths9, all_paths = count_paths_maze_with_paths(maze, start, end)

print(f"Maze: {maze}")
print(f"Start: {start}")
print(f"End: {end}")
print(f"Paths (recursive): {paths1}")
print(f"Paths (memoization): {paths2}")
print(f"Paths (DP): {paths3}")
print(f"Paths (with obstacles): {paths4}")
print(f"Paths (with diagonal): {paths5}")
print(f"Paths (with validation): {paths6}")
print(f"Paths (with optimization): {paths7}")
print(f"Paths (advanced optimization): {paths8}")
print(f"Paths (with paths): {paths9}, All paths: {all_paths}")
