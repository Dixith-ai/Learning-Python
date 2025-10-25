class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth_recursive(root):
    if not root:
        return 0
    
    left_depth = max_depth_recursive(root.left)
    right_depth = max_depth_recursive(root.right)
    
    return 1 + max(left_depth, right_depth)

def max_depth_iterative(root):
    if not root:
        return 0
    
    stack = [(root, 1)]
    max_depth = 0
    
    while stack:
        node, depth = stack.pop()
        max_depth = max(max_depth, depth)
        
        if node.left:
            stack.append((node.left, depth + 1))
        if node.right:
            stack.append((node.right, depth + 1))
    
    return max_depth

def max_depth_level_order(root):
    if not root:
        return 0
    
    depth = 0
    queue = [root]
    
    while queue:
        level_size = len(queue)
        depth += 1
        
        for _ in range(level_size):
            node = queue.pop(0)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return depth

def max_depth_bfs(root):
    if not root:
        return 0
    
    from collections import deque
    queue = deque([(root, 1)])
    max_depth = 0
    
    while queue:
        node, depth = queue.popleft()
        max_depth = max(max_depth, depth)
        
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    
    return max_depth

def max_depth_with_path(root):
    def dfs(node, current_depth):
        if not node:
            return current_depth - 1
        
        left_depth = dfs(node.left, current_depth + 1)
        right_depth = dfs(node.right, current_depth + 1)
        
        return max(left_depth, right_depth)
    
    return dfs(root, 1)

def max_depth_optimized(root):
    if not root:
        return 0
    
    return 1 + max(max_depth_optimized(root.left), max_depth_optimized(root.right))

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
root.right.right.left = TreeNode(1)

depth1 = max_depth_recursive(root)
depth2 = max_depth_iterative(root)
depth3 = max_depth_level_order(root)
depth4 = max_depth_bfs(root)
depth5 = max_depth_with_path(root)
depth6 = max_depth_optimized(root)

print(f"Max depth (recursive): {depth1}")
print(f"Max depth (iterative): {depth2}")
print(f"Max depth (level order): {depth3}")
print(f"Max depth (BFS): {depth4}")
print(f"Max depth (with path): {depth5}")
print(f"Max depth (optimized): {depth6}")
