class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameter_of_binary_tree(root):
    def height(node):
        if not node:
            return 0
        
        left_height = height(node.left)
        right_height = height(node.right)
        
        return 1 + max(left_height, right_height)
    
    def diameter(node):
        if not node:
            return 0
        
        left_diameter = diameter(node.left)
        right_diameter = diameter(node.right)
        
        left_height = height(node.left)
        right_height = height(node.right)
        
        return max(left_diameter, right_diameter, left_height + right_height)
    
    return diameter(root)

def diameter_of_binary_tree_optimized(root):
    max_diameter = 0
    
    def height(node):
        nonlocal max_diameter
        if not node:
            return 0
        
        left_height = height(node.left)
        right_height = height(node.right)
        
        max_diameter = max(max_diameter, left_height + right_height)
        
        return 1 + max(left_height, right_height)
    
    height(root)
    return max_diameter

def diameter_of_binary_tree_iterative(root):
    if not root:
        return 0
    
    max_diameter = 0
    stack = [(root, False)]
    heights = {}
    
    while stack:
        node, processed = stack.pop()
        
        if processed:
            left_height = heights.get(node.left, 0)
            right_height = heights.get(node.right, 0)
            
            max_diameter = max(max_diameter, left_height + right_height)
            heights[node] = 1 + max(left_height, right_height)
        else:
            stack.append((node, True))
            if node.right:
                stack.append((node.right, False))
            if node.left:
                stack.append((node.left, False))
    
    return max_diameter

def diameter_with_path(root):
    def dfs(node):
        if not node:
            return 0, []
        
        left_height, left_path = dfs(node.left)
        right_height, right_path = dfs(node.right)
        
        current_path = left_path + [node.val] + right_path
        
        if left_height + right_height > len(current_path) - 1:
            return left_height + right_height, current_path
        else:
            return left_height + right_height, current_path
    
    diameter, path = dfs(root)
    return diameter, path

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

diameter1 = diameter_of_binary_tree(root)
diameter2 = diameter_of_binary_tree_optimized(root)
diameter3 = diameter_of_binary_tree_iterative(root)
diameter4, path = diameter_with_path(root)

print(f"Diameter: {diameter1}")
print(f"Diameter (optimized): {diameter2}")
print(f"Diameter (iterative): {diameter3}")
print(f"Diameter with path: {diameter4}, Path: {path}")
