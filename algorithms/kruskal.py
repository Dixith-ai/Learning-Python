class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        
        return True

def kruskal_adjacency_list(graph):
    edges = []
    for u in graph:
        for v, weight in graph[u]:
            edges.append((weight, u, v))
    
    edges.sort()
    n = len(graph)
    uf = UnionFind(n)
    mst = []
    
    for weight, u, v in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
            if len(mst) == n - 1:
                break
    
    return mst

def kruskal_edge_list(edges, num_vertices):
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(num_vertices)
    mst = []
    
    for u, v, weight in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
            if len(mst) == num_vertices - 1:
                break
    
    return mst

def kruskal_adjacency_matrix(matrix):
    n = len(matrix)
    edges = []
    
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] > 0:
                edges.append((i, j, matrix[i][j]))
    
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    mst = []
    
    for u, v, weight in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
            if len(mst) == n - 1:
                break
    
    return mst

def kruskal_with_path_compression(graph):
    edges = []
    for u in graph:
        for v, weight in graph[u]:
            edges.append((weight, u, v))
    
    edges.sort()
    n = len(graph)
    parent = list(range(n))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False
        parent[px] = py
        return True
    
    mst = []
    for weight, u, v in edges:
        if union(u, v):
            mst.append((u, v, weight))
            if len(mst) == n - 1:
                break
    
    return mst

graph = {
    0: [(1, 4), (2, 2)],
    1: [(0, 4), (2, 1), (3, 5)],
    2: [(0, 2), (1, 1), (3, 8)],
    3: [(1, 5), (2, 8)]
}

edges = [(0, 1, 4), (0, 2, 2), (1, 2, 1), (1, 3, 5), (2, 3, 8)]

matrix = [
    [0, 4, 2, 0],
    [4, 0, 1, 5],
    [2, 1, 0, 8],
    [0, 5, 8, 0]
]

mst1 = kruskal_adjacency_list(graph)
mst2 = kruskal_edge_list(edges, 4)
mst3 = kruskal_adjacency_matrix(matrix)
mst4 = kruskal_with_path_compression(graph)

print(f"MST (adjacency list): {mst1}")
print(f"MST (edge list): {mst2}")
print(f"MST (adjacency matrix): {mst3}")
print(f"MST (path compression): {mst4}")
