from collections import deque, defaultdict

def topological_sort_kahn(graph):
    in_degree = defaultdict(int)
    
    for vertex in graph:
        for neighbor in graph[vertex]:
            in_degree[neighbor] += 1
    
    queue = deque([v for v in graph if in_degree[v] == 0])
    result = []
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        for neighbor in graph[vertex]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return result if len(result) == len(graph) else None

def topological_sort_dfs(graph):
    visited = set()
    temp_visited = set()
    result = []
    
    def dfs(vertex):
        if vertex in temp_visited:
            return False
        if vertex in visited:
            return True
        
        temp_visited.add(vertex)
        
        for neighbor in graph[vertex]:
            if not dfs(neighbor):
                return False
        
        temp_visited.remove(vertex)
        visited.add(vertex)
        result.append(vertex)
        return True
    
    for vertex in graph:
        if vertex not in visited:
            if not dfs(vertex):
                return None
    
    return result[::-1]

def topological_sort_matrix(matrix):
    n = len(matrix)
    in_degree = [0] * n
    
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                in_degree[j] += 1
    
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    result = []
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        for i in range(n):
            if matrix[vertex][i] == 1:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    queue.append(i)
    
    return result if len(result) == n else None

def topological_sort_all(graph):
    visited = set()
    temp_visited = set()
    result = []
    
    def dfs(vertex):
        if vertex in temp_visited:
            return False
        if vertex in visited:
            return True
        
        temp_visited.add(vertex)
        
        for neighbor in graph[vertex]:
            if not dfs(neighbor):
                return False
        
        temp_visited.remove(vertex)
        visited.add(vertex)
        result.append(vertex)
        return True
    
    for vertex in graph:
        if vertex not in visited:
            if not dfs(vertex):
                return None
    
    return result[::-1]

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': ['E'],
    'E': []
}

matrix = [
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0]
]

kahn_result = topological_sort_kahn(graph)
dfs_result = topological_sort_dfs(graph)
matrix_result = topological_sort_matrix(matrix)

print(f"Topological sort (Kahn): {kahn_result}")
print(f"Topological sort (DFS): {dfs_result}")
print(f"Topological sort (matrix): {matrix_result}")
