import heapq

def dijkstra_adjacency_list(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]
    previous = {}
    
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))
    
    return distances, previous

def dijkstra_adjacency_matrix(matrix, start):
    n = len(matrix)
    distances = [float('infinity')] * n
    distances[start] = 0
    visited = set()
    previous = {}
    
    for _ in range(n):
        u = min((i for i in range(n) if i not in visited), key=lambda x: distances[x])
        visited.add(u)
        
        for v in range(n):
            if matrix[u][v] > 0 and v not in visited:
                alt = distances[u] + matrix[u][v]
                if alt < distances[v]:
                    distances[v] = alt
                    previous[v] = u
    
    return distances, previous

def dijkstra_shortest_path(graph, start, end):
    distances, previous = dijkstra_adjacency_list(graph, start)
    
    if distances[end] == float('infinity'):
        return None, None
    
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous.get(current)
    
    return path[::-1], distances[end]

def dijkstra_all_pairs(graph):
    all_distances = {}
    
    for start in graph:
        distances, _ = dijkstra_adjacency_list(graph, start)
        all_distances[start] = distances
    
    return all_distances

graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('C', 1), ('D', 5)],
    'C': [('D', 8), ('E', 10)],
    'D': [('E', 2)],
    'E': []
}

matrix = [
    [0, 4, 2, 0, 0],
    [0, 0, 1, 5, 0],
    [0, 0, 0, 8, 10],
    [0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0]
]

distances, previous = dijkstra_adjacency_list(graph, 'A')
distances_matrix, previous_matrix = dijkstra_adjacency_matrix(matrix, 0)
path, distance = dijkstra_shortest_path(graph, 'A', 'E')
all_pairs = dijkstra_all_pairs(graph)

print(f"Distances from A: {distances}")
print(f"Previous vertices: {previous}")
print(f"Distances (matrix): {distances_matrix}")
print(f"Shortest path A to E: {path} (distance: {distance})")
print(f"All pairs distances: {all_pairs}")
