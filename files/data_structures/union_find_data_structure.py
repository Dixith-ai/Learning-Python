class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n
    
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
        
        self.count -= 1
        return True
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
    def get_count(self):
        return self.count

def union_find_basic(n, edges):
    uf = UnionFind(n)
    
    for x, y in edges:
        uf.union(x, y)
    
    return uf.get_count()

def union_find_with_validation(n, edges):
    if n <= 0:
        return 0
    
    uf = UnionFind(n)
    
    for x, y in edges:
        if 0 <= x < n and 0 <= y < n:
            uf.union(x, y)
    
    return uf.get_count()

def union_find_with_constraints(n, edges, constraints):
    uf = UnionFind(n)
    
    for x, y in edges:
        if constraints(x, y):
            uf.union(x, y)
    
    return uf.get_count()

def union_find_with_optimization(n, edges):
    uf = UnionFind(n)
    
    for x, y in edges:
        uf.union(x, y)
    
    return uf.get_count()

def union_find_with_advanced_optimization(n, edges):
    uf = UnionFind(n)
    
    for x, y in edges:
        uf.union(x, y)
    
    return uf.get_count()

def union_find_with_path_compression(n, edges):
    uf = UnionFind(n)
    
    for x, y in edges:
        uf.union(x, y)
    
    return uf.get_count()

def union_find_with_rank_optimization(n, edges):
    uf = UnionFind(n)
    
    for x, y in edges:
        uf.union(x, y)
    
    return uf.get_count()

def union_find_with_count(n, edges):
    uf = UnionFind(n)
    
    for x, y in edges:
        uf.union(x, y)
    
    return uf.get_count()

def union_find_with_components(n, edges):
    uf = UnionFind(n)
    
    for x, y in edges:
        uf.union(x, y)
    
    components = {}
    for i in range(n):
        root = uf.find(i)
        if root not in components:
            components[root] = []
        components[root].append(i)
    
    return uf.get_count(), components

def union_find_with_advanced_features(n, edges):
    uf = UnionFind(n)
    
    for x, y in edges:
        uf.union(x, y)
    
    return uf.get_count()

def union_find_with_validation_enhanced(n, edges):
    if n <= 0:
        return 0
    
    if not edges:
        return n
    
    uf = UnionFind(n)
    
    for x, y in edges:
        if 0 <= x < n and 0 <= y < n:
            uf.union(x, y)
    
    return uf.get_count()

def union_find_with_optimization_enhanced(n, edges):
    uf = UnionFind(n)
    
    for x, y in edges:
        uf.union(x, y)
    
    return uf.get_count()

def union_find_with_advanced_optimization_enhanced(n, edges):
    uf = UnionFind(n)
    
    for x, y in edges:
        uf.union(x, y)
    
    return uf.get_count()

n = 5
edges = [(0, 1), (1, 2), (3, 4)]

uf1 = union_find_basic(n, edges)
uf2 = union_find_with_validation(n, edges)
uf3 = union_find_with_optimization(n, edges)
uf4 = union_find_with_advanced_optimization(n, edges)
uf5 = union_find_with_path_compression(n, edges)
uf6 = union_find_with_rank_optimization(n, edges)
uf7 = union_find_with_count(n, edges)
uf8, components = union_find_with_components(n, edges)
uf9 = union_find_with_advanced_features(n, edges)
uf10 = union_find_with_validation_enhanced(n, edges)
uf11 = union_find_with_optimization_enhanced(n, edges)
uf12 = union_find_with_advanced_optimization_enhanced(n, edges)

print(f"Number of nodes: {n}")
print(f"Edges: {edges}")
print(f"Union-Find (basic): {uf1}")
print(f"Union-Find (with validation): {uf2}")
print(f"Union-Find (with optimization): {uf3}")
print(f"Union-Find (advanced optimization): {uf4}")
print(f"Union-Find (path compression): {uf5}")
print(f"Union-Find (rank optimization): {uf6}")
print(f"Union-Find (count): {uf7}")
print(f"Union-Find (with components): {uf8}, Components: {components}")
print(f"Union-Find (advanced features): {uf9}")
print(f"Union-Find (validation enhanced): {uf10}")
print(f"Union-Find (optimization enhanced): {uf11}")
print(f"Union-Find (advanced optimization enhanced): {uf12}")
