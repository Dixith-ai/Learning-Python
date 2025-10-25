class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def height_binary_tree_recursive(root):
    if not root:
        return 0
    
    left_height = height_binary_tree_recursive(root.left)
    right_height = height_binary_tree_recursive(root.right)
    
    return 1 + max(left_height, right_height)

def height_binary_tree_iterative(root):
    if not root:
        return 0
    
    queue = [(root, 1)]
    max_height = 0
    
    while queue:
        node, height = queue.pop(0)
        max_height = max(max_height, height)
        
        if node.left:
            queue.append((node.left, height + 1))
        if node.right:
            queue.append((node.right, height + 1))
    
    return max_height

def height_binary_tree_level_order(root):
    if not root:
        return 0
    
    height = 0
    queue = [root]
    
    while queue:
        level_size = len(queue)
        height += 1
        
        for _ in range(level_size):
            node = queue.pop(0)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return height

def height_binary_tree_stack(root):
    if not root:
        return 0
    
    stack = [(root, 1)]
    max_height = 0
    
    while stack:
        node, height = stack.pop()
        max_height = max(max_height, height)
        
        if node.right:
            stack.append((node.right, height + 1))
        if node.left:
            stack.append((node.left, height + 1))
    
    return max_height

def height_binary_tree_with_path(root):
    def dfs(node, current_height):
        if not node:
            return current_height - 1
        
        left_height = dfs(node.left, current_height + 1)
        right_height = dfs(node.right, current_height + 1)
        
        return max(left_height, right_height)
    
    return dfs(root, 1)

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
root.right.right.left = TreeNode(1)

height1 = height_binary_tree_recursive(root)
height2 = height_binary_tree_iterative(root)
height3 = height_binary_tree_level_order(root)
height4 = height_binary_tree_stack(root)
height5 = height_binary_tree_with_path(root)

print(f"Height (recursive): {height1}")
print(f"Height (iterative): {height2}")
print(f"Height (level order): {height3}")
print(f"Height (stack): {height4}")
print(f"Height (with path): {height5}")
