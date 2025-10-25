class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lca_bst_recursive(root, p, q):
    if not root:
        return None
    
    if p.val < root.val and q.val < root.val:
        return lca_bst_recursive(root.left, p, q)
    elif p.val > root.val and q.val > root.val:
        return lca_bst_recursive(root.right, p, q)
    else:
        return root

def lca_bst_iterative(root, p, q):
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root
    
    return None

def lca_bst_optimized(root, p, q):
    if not root:
        return None
    
    min_val = min(p.val, q.val)
    max_val = max(p.val, q.val)
    
    while root:
        if root.val >= min_val and root.val <= max_val:
            return root
        elif root.val > max_val:
            root = root.left
        else:
            root = root.right
    
    return None

def lca_bst_with_path(root, p, q):
    def find_path(node, target):
        path = []
        while node:
            path.append(node)
            if target.val == node.val:
                break
            elif target.val < node.val:
                node = node.left
            else:
                node = node.right
        return path
    
    path_p = find_path(root, p)
    path_q = find_path(root, q)
    
    if not path_p or not path_q:
        return None
    
    i = 0
    while i < len(path_p) and i < len(path_q) and path_p[i] == path_q[i]:
        i += 1
    
    return path_p[i - 1] if i > 0 else None

def lca_bst_with_validation(root, p, q):
    if not root or not p or not q:
        return None
    
    def is_node_in_tree(node, target):
        if not node:
            return False
        
        if node.val == target.val:
            return True
        
        if target.val < node.val:
            return is_node_in_tree(node.left, target)
        else:
            return is_node_in_tree(node.right, target)
    
    if not is_node_in_tree(root, p) or not is_node_in_tree(root, q):
        return None
    
    return lca_bst_recursive(root, p, q)

def lca_bst_with_distance(root, p, q):
    def find_distance(node, target):
        distance = 0
        while node and node.val != target.val:
            if target.val < node.val:
                node = node.left
            else:
                node = node.right
            distance += 1
        return distance if node else -1
    
    if not root:
        return None
    
    dist_p = find_distance(root, p)
    dist_q = find_distance(root, q)
    
    if dist_p == -1 or dist_q == -1:
        return None
    
    current = root
    while current:
        if p.val < current.val and q.val < current.val:
            current = current.left
        elif p.val > current.val and q.val > current.val:
            current = current.right
        else:
            return current
    
    return None

def lca_bst_with_level(root, p, q):
    def get_level(node, target):
        level = 0
        while node and node.val != target.val:
            if target.val < node.val:
                node = node.left
            else:
                node = node.right
            level += 1
        return level if node else -1
    
    if not root:
        return None
    
    level_p = get_level(root, p)
    level_q = get_level(root, q)
    
    if level_p == -1 or level_q == -1:
        return None
    
    return lca_bst_recursive(root, p, q)

def lca_bst_with_parent_pointer(root, p, q):
    def find_path_with_parent(node, target):
        path = []
        while node:
            path.append(node)
            if target.val == node.val:
                break
            elif target.val < node.val:
                node = node.left
            else:
                node = node.right
        return path
    
    path_p = find_path_with_parent(root, p)
    path_q = find_path_with_parent(root, q)
    
    if not path_p or not path_q:
        return None
    
    i = 0
    while i < len(path_p) and i < len(path_q) and path_p[i] == path_q[i]:
        i += 1
    
    return path_p[i - 1] if i > 0 else None

def lca_bst_with_ancestors(root, p, q):
    def get_ancestors(node, target):
        ancestors = []
        while node:
            ancestors.append(node)
            if target.val == node.val:
                break
            elif target.val < node.val:
                node = node.left
            else:
                node = node.right
        return ancestors
    
    ancestors_p = get_ancestors(root, p)
    ancestors_q = get_ancestors(root, q)
    
    if not ancestors_p or not ancestors_q:
        return None
    
    i = 0
    while i < len(ancestors_p) and i < len(ancestors_q) and ancestors_p[i] == ancestors_q[i]:
        i += 1
    
    return ancestors_p[i - 1] if i > 0 else None

def create_bst(values):
    if not values:
        return None
    
    root = TreeNode(values[0])
    
    for val in values[1:]:
        insert_into_bst(root, val)
    
    return root

def insert_into_bst(root, val):
    if val < root.val:
        if root.left:
            insert_into_bst(root.left, val)
        else:
            root.left = TreeNode(val)
    else:
        if root.right:
            insert_into_bst(root.right, val)
        else:
            root.right = TreeNode(val)

def inorder_traversal(root):
    if not root:
        return []
    
    result = []
    result.extend(inorder_traversal(root.left))
    result.append(root.val)
    result.extend(inorder_traversal(root.right))
    return result

values = [6, 2, 8, 0, 4, 7, 9, 3, 5]
root = create_bst(values)

p = TreeNode(2)
q = TreeNode(8)

lca1 = lca_bst_recursive(root, p, q)
lca2 = lca_bst_iterative(root, p, q)
lca3 = lca_bst_optimized(root, p, q)
lca4 = lca_bst_with_path(root, p, q)
lca5 = lca_bst_with_validation(root, p, q)
lca6 = lca_bst_with_distance(root, p, q)
lca7 = lca_bst_with_level(root, p, q)
lca8 = lca_bst_with_parent_pointer(root, p, q)
lca9 = lca_bst_with_ancestors(root, p, q)

print(f"BST values: {values}")
print(f"Inorder traversal: {inorder_traversal(root)}")
print(f"LCA of {p.val} and {q.val} (recursive): {lca1.val if lca1 else None}")
print(f"LCA of {p.val} and {q.val} (iterative): {lca2.val if lca2 else None}")
print(f"LCA of {p.val} and {q.val} (optimized): {lca3.val if lca3 else None}")
print(f"LCA of {p.val} and {q.val} (with path): {lca4.val if lca4 else None}")
print(f"LCA of {p.val} and {q.val} (with validation): {lca5.val if lca5 else None}")
print(f"LCA of {p.val} and {q.val} (with distance): {lca6.val if lca6 else None}")
print(f"LCA of {p.val} and {q.val} (with level): {lca7.val if lca7 else None}")
print(f"LCA of {p.val} and {q.val} (with parent): {lca8.val if lca8 else None}")
print(f"LCA of {p.val} and {q.val} (with ancestors): {lca9.val if lca9 else None}")
