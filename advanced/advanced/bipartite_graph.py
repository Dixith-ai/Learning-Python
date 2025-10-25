from collections import deque

def is_bipartite_bfs(graph):
    color = {}
    
    for start in graph:
        if start not in color:
            queue = deque([start])
            color[start] = 0
            
            while queue:
                vertex = queue.popleft()
                
                for neighbor in graph[vertex]:
                    if neighbor in color:
                        if color[neighbor] == color[vertex]:
                            return False
                    else:
                        color[neighbor] = 1 - color[vertex]
                        queue.append(neighbor)
    
    return True

def is_bipartite_dfs(graph):
    color = {}
    
    def dfs(vertex, c):
        if vertex in color:
            return color[vertex] == c
        
        color[vertex] = c
        
        for neighbor in graph[vertex]:
            if not dfs(neighbor, 1 - c):
                return False
        
        return True
    
    for start in graph:
        if start not in color:
            if not dfs(start, 0):
                return False
    
    return True

def is_bipartite_adjacency_matrix(matrix):
    n = len(matrix)
    color = [-1] * n
    
    for start in range(n):
        if color[start] == -1:
            queue = deque([start])
            color[start] = 0
            
            while queue:
                vertex = queue.popleft()
                
                for i in range(n):
                    if matrix[vertex][i] == 1:
                        if color[i] == -1:
                            color[i] = 1 - color[vertex]
                            queue.append(i)
                        elif color[i] == color[vertex]:
                            return False
    
    return True

def bipartite_coloring(graph):
    color = {}
    
    for start in graph:
        if start not in color:
            queue = deque([start])
            color[start] = 0
            
            while queue:
                vertex = queue.popleft()
                
                for neighbor in graph[vertex]:
                    if neighbor in color:
                        if color[neighbor] == color[vertex]:
                            return None
                    else:
                        color[neighbor] = 1 - color[vertex]
                        queue.append(neighbor)
    
    return color

graph1 = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3],
    3: [0, 2]
}

graph2 = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1]
}

matrix = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
]

bipartite1 = is_bipartite_bfs(graph1)
bipartite2 = is_bipartite_dfs(graph2)
bipartite3 = is_bipartite_adjacency_matrix(matrix)
coloring = bipartite_coloring(graph1)

print(f"Graph 1 is bipartite (BFS): {bipartite1}")
print(f"Graph 2 is bipartite (DFS): {bipartite2}")
print(f"Matrix is bipartite: {bipartite3}")
print(f"Bipartite coloring: {coloring}")
