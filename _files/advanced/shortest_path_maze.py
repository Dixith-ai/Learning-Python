from collections import deque

def shortest_path_maze_bfs(maze, start, end):
    if not maze or not maze[0]:
        return -1
    
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    queue = deque([(start[0], start[1], 0)])
    visited = {(start[0], start[1])}
    
    while queue:
        row, col, distance = queue.popleft()
        
        if (row, col) == end:
            return distance
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < rows and 0 <= new_col < cols and
                maze[new_row][new_col] == 0 and
                (new_row, new_col) not in visited):
                
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, distance + 1))
    
    return -1

def shortest_path_maze_dfs(maze, start, end):
    if not maze or not maze[0]:
        return -1
    
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    def dfs(row, col, distance, visited):
        if (row, col) == end:
            return distance
        
        min_distance = float('inf')
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < rows and 0 <= new_col < cols and
                maze[new_row][new_col] == 0 and
                (new_row, new_col) not in visited):
                
                visited.add((new_row, new_col))
                result = dfs(new_row, new_col, distance + 1, visited)
                if result != -1:
                    min_distance = min(min_distance, result)
                visited.remove((new_row, new_col))
        
        return min_distance if min_distance != float('inf') else -1
    
    return dfs(start[0], start[1], 0, {(start[0], start[1])})

def shortest_path_maze_optimized(maze, start, end):
    if not maze or not maze[0]:
        return -1
    
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    queue = deque([(start[0], start[1], 0)])
    visited = {(start[0], start[1])}
    
    while queue:
        row, col, distance = queue.popleft()
        
        if (row, col) == end:
            return distance
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < rows and 0 <= new_col < cols and
                maze[new_row][new_col] == 0 and
                (new_row, new_col) not in visited):
                
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, distance + 1))
    
    return -1

def shortest_path_maze_with_validation(maze, start, end):
    if not maze or not maze[0]:
        return -1
    
    if not (0 <= start[0] < len(maze) and 0 <= start[1] < len(maze[0])):
        return -1
    
    if not (0 <= end[0] < len(maze) and 0 <= end[1] < len(maze[0])):
        return -1
    
    if maze[start[0]][start[1]] == 1 or maze[end[0]][end[1]] == 1:
        return -1
    
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    queue = deque([(start[0], start[1], 0)])
    visited = {(start[0], start[1])}
    
    while queue:
        row, col, distance = queue.popleft()
        
        if (row, col) == end:
            return distance
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < rows and 0 <= new_col < cols and
                maze[new_row][new_col] == 0 and
                (new_row, new_col) not in visited):
                
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, distance + 1))
    
    return -1

def shortest_path_maze_with_constraints(maze, start, end, constraints):
    if not maze or not maze[0]:
        return -1
    
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    queue = deque([(start[0], start[1], 0)])
    visited = {(start[0], start[1])}
    
    while queue:
        row, col, distance = queue.popleft()
        
        if (row, col) == end:
            return distance
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < rows and 0 <= new_col < cols and
                maze[new_row][new_col] == 0 and
                (new_row, new_col) not in visited and
                constraints(new_row, new_col)):
                
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, distance + 1))
    
    return -1

def shortest_path_maze_with_optimization(maze, start, end):
    if not maze or not maze[0]:
        return -1
    
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    queue = deque([(start[0], start[1], 0)])
    visited = {(start[0], start[1])}
    
    while queue:
        row, col, distance = queue.popleft()
        
        if (row, col) == end:
            return distance
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < rows and 0 <= new_col < cols and
                maze[new_row][new_col] == 0 and
                (new_row, new_col) not in visited):
                
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, distance + 1))
    
    return -1

def shortest_path_maze_with_advanced_optimization(maze, start, end):
    if not maze or not maze[0]:
        return -1
    
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    queue = deque([(start[0], start[1], 0)])
    visited = {(start[0], start[1])}
    
    while queue:
        row, col, distance = queue.popleft()
        
        if (row, col) == end:
            return distance
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < rows and 0 <= new_col < cols and
                maze[new_row][new_col] == 0 and
                (new_row, new_col) not in visited):
                
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, distance + 1))
    
    return -1

def shortest_path_maze_with_count(maze, start, end):
    if not maze or not maze[0]:
        return -1, 0
    
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    queue = deque([(start[0], start[1], 0)])
    visited = {(start[0], start[1])}
    count = 0
    
    while queue:
        row, col, distance = queue.popleft()
        count += 1
        
        if (row, col) == end:
            return distance, count
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < rows and 0 <= new_col < cols and
                maze[new_row][new_col] == 0 and
                (new_row, new_col) not in visited):
                
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, distance + 1))
    
    return -1, count

def shortest_path_maze_with_path(maze, start, end):
    if not maze or not maze[0]:
        return -1, []
    
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    queue = deque([(start[0], start[1], 0, [(start[0], start[1])])])
    visited = {(start[0], start[1])}
    
    while queue:
        row, col, distance, path = queue.popleft()
        
        if (row, col) == end:
            return distance, path
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < rows and 0 <= new_col < cols and
                maze[new_row][new_col] == 0 and
                (new_row, new_col) not in visited):
                
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, distance + 1, path + [(new_row, new_col)]))
    
    return -1, []

def shortest_path_maze_with_negative(maze, start, end):
    if not maze or not maze[0]:
        return -1
    
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    queue = deque([(start[0], start[1], 0)])
    visited = {(start[0], start[1])}
    
    while queue:
        row, col, distance = queue.popleft()
        
        if (row, col) == end:
            return distance
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < rows and 0 <= new_col < cols and
                maze[new_row][new_col] == 0 and
                (new_row, new_col) not in visited):
                
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, distance + 1))
    
    return -1

def shortest_path_maze_with_circular(maze, start, end):
    if not maze or not maze[0]:
        return -1
    
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    queue = deque([(start[0], start[1], 0)])
    visited = {(start[0], start[1])}
    
    while queue:
        row, col, distance = queue.popleft()
        
        if (row, col) == end:
            return distance
        
        for dr, dc in directions:
            new_row, new_col = (row + dr) % rows, (col + dc) % cols
            
            if (maze[new_row][new_col] == 0 and
                (new_row, new_col) not in visited):
                
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, distance + 1))
    
    return -1

def shortest_path_maze_with_validation_enhanced(maze, start, end):
    if not maze or not maze[0]:
        return -1
    
    if not (0 <= start[0] < len(maze) and 0 <= start[1] < len(maze[0])):
        return -1
    
    if not (0 <= end[0] < len(maze) and 0 <= end[1] < len(maze[0])):
        return -1
    
    if maze[start[0]][start[1]] == 1 or maze[end[0]][end[1]] == 1:
        return -1
    
    if start == end:
        return 0
    
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    queue = deque([(start[0], start[1], 0)])
    visited = {(start[0], start[1])}
    
    while queue:
        row, col, distance = queue.popleft()
        
        if (row, col) == end:
            return distance
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < rows and 0 <= new_col < cols and
                maze[new_row][new_col] == 0 and
                (new_row, new_col) not in visited):
                
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, distance + 1))
    
    return -1

def shortest_path_maze_with_optimization_enhanced(maze, start, end):
    if not maze or not maze[0]:
        return -1
    
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    queue = deque([(start[0], start[1], 0)])
    visited = {(start[0], start[1])}
    
    while queue:
        row, col, distance = queue.popleft()
        
        if (row, col) == end:
            return distance
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < rows and 0 <= new_col < cols and
                maze[new_row][new_col] == 0 and
                (new_row, new_col) not in visited):
                
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, distance + 1))
    
    return -1

def shortest_path_maze_with_advanced_optimization_enhanced(maze, start, end):
    if not maze or not maze[0]:
        return -1
    
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    queue = deque([(start[0], start[1], 0)])
    visited = {(start[0], start[1])}
    
    while queue:
        row, col, distance = queue.popleft()
        
        if (row, col) == end:
            return distance
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < rows and 0 <= new_col < cols and
                maze[new_row][new_col] == 0 and
                (new_row, new_col) not in visited):
                
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, distance + 1))
    
    return -1

maze = [[0, 0, 0], [1, 1, 0], [0, 0, 0]]
start = (0, 0)
end = (2, 2)

path1 = shortest_path_maze_bfs(maze, start, end)
path2 = shortest_path_maze_dfs(maze, start, end)
path3 = shortest_path_maze_optimized(maze, start, end)
path4 = shortest_path_maze_with_validation(maze, start, end)
path5 = shortest_path_maze_with_optimization(maze, start, end)
path6 = shortest_path_maze_with_advanced_optimization(maze, start, end)
path7, count = shortest_path_maze_with_count(maze, start, end)
path8, path = shortest_path_maze_with_path(maze, start, end)
path9 = shortest_path_maze_with_negative(maze, start, end)
path10 = shortest_path_maze_with_circular(maze, start, end)
path11 = shortest_path_maze_with_validation_enhanced(maze, start, end)
path12 = shortest_path_maze_with_optimization_enhanced(maze, start, end)
path13 = shortest_path_maze_with_advanced_optimization_enhanced(maze, start, end)

print(f"Maze: {maze}")
print(f"Start: {start}")
print(f"End: {end}")
print(f"Shortest path (BFS): {path1}")
print(f"Shortest path (DFS): {path2}")
print(f"Shortest path (optimized): {path3}")
print(f"Shortest path (with validation): {path4}")
print(f"Shortest path (with optimization): {path5}")
print(f"Shortest path (advanced optimization): {path6}")
print(f"Shortest path (with count): {path7}, Count: {count}")
print(f"Shortest path (with path): {path8}, Path: {path}")
print(f"Shortest path (with negative): {path9}")
print(f"Shortest path (with circular): {path10}")
print(f"Shortest path (validation enhanced): {path11}")
print(f"Shortest path (optimization enhanced): {path12}")
print(f"Shortest path (advanced optimization enhanced): {path13}")
