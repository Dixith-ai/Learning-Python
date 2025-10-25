def dfs_adjacency_list(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    result = [start]
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            result.extend(dfs_adjacency_list(graph, neighbor, visited))
    
    return result

def dfs_adjacency_matrix(matrix, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    result = [start]
    n = len(matrix)
    
    for i in range(n):
        if matrix[start][i] == 1 and i not in visited:
            result.extend(dfs_adjacency_matrix(matrix, i, visited))
    
    return result

def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    result = []
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            
            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return result

def dfs_path_exists(graph, start, end, visited=None):
    if visited is None:
        visited = set()
    
    if start == end:
        return True
    
    visited.add(start)
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            if dfs_path_exists(graph, neighbor, end, visited):
                return True
    
    return False

def dfs_connected_components(graph):
    visited = set()
    components = []
    
    for vertex in graph:
        if vertex not in visited:
            component = dfs_adjacency_list(graph, vertex, visited)
            components.append(component)
    
    return components

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

dfs_recursive = dfs_adjacency_list(graph, 0)
dfs_matrix = dfs_adjacency_matrix(matrix, 0)
dfs_iter = dfs_iterative(graph, 0)
path_exists = dfs_path_exists(graph, 0, 5)
components = dfs_connected_components(graph)

print(f"DFS (recursive): {dfs_recursive}")
print(f"DFS (matrix): {dfs_matrix}")
print(f"DFS (iterative): {dfs_iter}")
print(f"Path exists from 0 to 5: {path_exists}")
print(f"Connected components: {components}")
