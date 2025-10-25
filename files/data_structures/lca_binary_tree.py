class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lca_recursive(root, p, q):
    if not root or root == p or root == q:
        return root
    
    left = lca_recursive(root.left, p, q)
    right = lca_recursive(root.right, p, q)
    
    if left and right:
        return root
    
    return left or right

def lca_iterative(root, p, q):
    if not root:
        return None
    
    parent = {root: None}
    stack = [root]
    
    while p not in parent or q not in parent:
        node = stack.pop()
        
        if node.left:
            parent[node.left] = node
            stack.append(node.left)
        
        if node.right:
            parent[node.right] = node
            stack.append(node.right)
    
    ancestors = set()
    while p:
        ancestors.add(p)
        p = parent[p]
    
    while q not in ancestors:
        q = parent[q]
    
    return q

def lca_with_path(root, p, q):
    def find_path(node, target, path):
        if not node:
            return False
        
        path.append(node)
        
        if node == target:
            return True
        
        if find_path(node.left, target, path) or find_path(node.right, target, path):
            return True
        
        path.pop()
        return False
    
    path_p = []
    path_q = []
    
    find_path(root, p, path_p)
    find_path(root, q, path_q)
    
    i = 0
    while i < len(path_p) and i < len(path_q) and path_p[i] == path_q[i]:
        i += 1
    
    return path_p[i - 1] if i > 0 else None

def lca_with_parent_pointer(node, p, q):
    def get_depth(n):
        depth = 0
        while n:
            depth += 1
            n = n.parent
        return depth
    
    depth_p = get_depth(p)
    depth_q = get_depth(q)
    
    while depth_p > depth_q:
        p = p.parent
        depth_p -= 1
    
    while depth_q > depth_p:
        q = q.parent
        depth_q -= 1
    
    while p != q:
        p = p.parent
        q = q.parent
    
    return p

def lca_bst(root, p, q):
    while root:
        if root.val > p.val and root.val > q.val:
            root = root.left
        elif root.val < p.val and root.val < q.val:
            root = root.right
        else:
            return root
    
    return None

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

p = root.left
q = root.right

lca1 = lca_recursive(root, p, q)
lca2 = lca_iterative(root, p, q)
lca3 = lca_with_path(root, p, q)

print(f"LCA of {p.val} and {q.val}: {lca1.val if lca1 else None}")
print(f"LCA (iterative): {lca2.val if lca2 else None}")
print(f"LCA (with path): {lca3.val if lca3 else None}")
