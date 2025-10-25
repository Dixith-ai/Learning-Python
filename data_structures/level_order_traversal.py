from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result

def level_order_traversal_single_list(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        result.append(node.val)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result

def level_order_traversal_recursive(root):
    result = []
    
    def dfs(node, level):
        if not node:
            return
        
        if level >= len(result):
            result.append([])
        
        result[level].append(node.val)
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)
    
    dfs(root, 0)
    return result

def level_order_traversal_zigzag(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    left_to_right = True
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            
            if left_to_right:
                level.append(node.val)
            else:
                level.insert(0, node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
        left_to_right = not left_to_right
    
    return result

def level_order_traversal_with_levels(root):
    if not root:
        return []
    
    result = []
    queue = deque([(root, 0)])
    
    while queue:
        node, level = queue.popleft()
        
        if level >= len(result):
            result.append([])
        
        result[level].append(node.val)
        
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))
    
    return result

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

level_order1 = level_order_traversal(root)
level_order2 = level_order_traversal_single_list(root)
level_order3 = level_order_traversal_recursive(root)
level_order4 = level_order_traversal_zigzag(root)
level_order5 = level_order_traversal_with_levels(root)

print(f"Level order (by levels): {level_order1}")
print(f"Level order (single list): {level_order2}")
print(f"Level order (recursive): {level_order3}")
print(f"Level order (zigzag): {level_order4}")
print(f"Level order (with levels): {level_order5}")
