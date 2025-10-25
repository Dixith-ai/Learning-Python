from collections import deque

def bfs_adjacency_list(graph, start):
    visited = set()
    queue = deque([start])
    result = []
    
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return result

def bfs_adjacency_matrix(matrix, start):
    n = len(matrix)
    visited = [False] * n
    queue = deque([start])
    result = []
    
    visited[start] = True
    result.append(start)
    
    while queue:
        vertex = queue.popleft()
        
        for i in range(n):
            if matrix[vertex][i] == 1 and not visited[i]:
                visited[i] = True
                result.append(i)
                queue.append(i)
    
    return result

def bfs_shortest_path(graph, start, end):
    if start == end:
        return [start]
    
    visited = set()
    queue = deque([(start, [start])])
    
    while queue:
        vertex, path = queue.popleft()
        
        for neighbor in graph[vertex]:
            if neighbor == end:
                return path + [neighbor]
            
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return None

def bfs_level_order(graph, start):
    visited = set()
    queue = deque([(start, 0)])
    levels = {}
    
    while queue:
        vertex, level = queue.popleft()
        
        if vertex not in visited:
            visited.add(vertex)
            levels[vertex] = level
            
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append((neighbor, level + 1))
    
    return levels

graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}

matrix = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0]
]

bfs_list = bfs_adjacency_list(graph, 0)
bfs_matrix = bfs_adjacency_matrix(matrix, 0)
shortest_path = bfs_shortest_path(graph, 0, 5)
levels = bfs_level_order(graph, 0)

print(f"BFS (adjacency list): {bfs_list}")
print(f"BFS (adjacency matrix): {bfs_matrix}")
print(f"Shortest path from 0 to 5: {shortest_path}")
print(f"Levels: {levels}")
