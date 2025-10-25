class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

def diameter_of_binary_tree_recursive(root):
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

def diameter_of_binary_tree_with_path(root):
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

def diameter_of_binary_tree_with_nodes(root):
    max_diameter = 0
    max_path = []
    
    def dfs(node):
        nonlocal max_diameter, max_path
        
        if not node:
            return 0, []
        
        left_height, left_path = dfs(node.left)
        right_height, right_path = dfs(node.right)
        
        current_path = left_path + [node.val] + right_path
        current_diameter = left_height + right_height
        
        if current_diameter > max_diameter:
            max_diameter = current_diameter
            max_path = current_path
        
        return 1 + max(left_height, right_height), current_path
    
    dfs(root)
    return max_diameter, max_path

def diameter_of_binary_tree_with_validation(root):
    if not root:
        return 0
    
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

def diameter_of_binary_tree_with_level(root):
    if not root:
        return 0
    
    level_diameters = {}
    
    def dfs(node, level):
        if not node:
            return 0
        
        left_height = dfs(node.left, level + 1)
        right_height = dfs(node.right, level + 1)
        
        current_diameter = left_height + right_height
        level_diameters[level] = max(level_diameters.get(level, 0), current_diameter)
        
        return 1 + max(left_height, right_height)
    
    dfs(root, 0)
    return max(level_diameters.values())

def diameter_of_binary_tree_with_count(root):
    if not root:
        return 0
    
    def count_nodes(node):
        if not node:
            return 0
        return 1 + count_nodes(node.left) + count_nodes(node.right)
    
    def diameter(node):
        if not node:
            return 0
        
        left_diameter = diameter(node.left)
        right_diameter = diameter(node.right)
        
        left_count = count_nodes(node.left)
        right_count = count_nodes(node.right)
        
        return max(left_diameter, right_diameter, left_count + right_count)
    
    return diameter(root)

def diameter_of_binary_tree_with_odd_even(root):
    if not root:
        return 0
    
    odd_diameter = 0
    even_diameter = 0
    
    def dfs(node, level):
        nonlocal odd_diameter, even_diameter
        
        if not node:
            return 0
        
        left_height = dfs(node.left, level + 1)
        right_height = dfs(node.right, level + 1)
        
        current_diameter = left_height + right_height
        
        if level % 2 == 0:
            even_diameter = max(even_diameter, current_diameter)
        else:
            odd_diameter = max(odd_diameter, current_diameter)
        
        return 1 + max(left_height, right_height)
    
    dfs(root, 0)
    return max(odd_diameter, even_diameter)

def diameter_of_binary_tree_with_positive_negative(root):
    if not root:
        return 0
    
    positive_diameter = 0
    negative_diameter = 0
    
    def dfs(node):
        nonlocal positive_diameter, negative_diameter
        
        if not node:
            return 0
        
        left_height = dfs(node.left)
        right_height = dfs(node.right)
        
        current_diameter = left_height + right_height
        
        if node.val >= 0:
            positive_diameter = max(positive_diameter, current_diameter)
        else:
            negative_diameter = max(negative_diameter, current_diameter)
        
        return 1 + max(left_height, right_height)
    
    dfs(root)
    return max(positive_diameter, negative_diameter)

def diameter_of_binary_tree_with_range(root, min_val, max_val):
    if not root:
        return 0
    
    def dfs(node):
        if not node:
            return 0
        
        if not (min_val <= node.val <= max_val):
            return 0
        
        left_height = dfs(node.left)
        right_height = dfs(node.right)
        
        return 1 + max(left_height, right_height)
    
    def diameter(node):
        if not node:
            return 0
        
        if not (min_val <= node.val <= max_val):
            return 0
        
        left_diameter = diameter(node.left)
        right_diameter = diameter(node.right)
        
        left_height = dfs(node.left)
        right_height = dfs(node.right)
        
        return max(left_diameter, right_diameter, left_height + right_height)
    
    return diameter(root)

def create_binary_tree(values):
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    
    while queue and i < len(values):
        node = queue.pop(0)
        
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root

def inorder_traversal(root):
    if not root:
        return []
    
    result = []
    result.extend(inorder_traversal(root.left))
    result.append(root.val)
    result.extend(inorder_traversal(root.right))
    return result

values = [1, 2, 3, 4, 5, 6, 7]
root = create_binary_tree(values)

diameter1 = diameter_of_binary_tree_optimized(root)
diameter2 = diameter_of_binary_tree_recursive(root)
diameter3 = diameter_of_binary_tree_iterative(root)
diameter4, path = diameter_of_binary_tree_with_path(root)
diameter5, max_path = diameter_of_binary_tree_with_nodes(root)
diameter6 = diameter_of_binary_tree_with_validation(root)
diameter7 = diameter_of_binary_tree_with_level(root)
diameter8 = diameter_of_binary_tree_with_count(root)
diameter9 = diameter_of_binary_tree_with_odd_even(root)
diameter10 = diameter_of_binary_tree_with_positive_negative(root)
diameter11 = diameter_of_binary_tree_with_range(root, 1, 5)

print(f"Binary tree values: {values}")
print(f"Inorder traversal: {inorder_traversal(root)}")
print(f"Diameter (optimized): {diameter1}")
print(f"Diameter (recursive): {diameter2}")
print(f"Diameter (iterative): {diameter3}")
print(f"Diameter (with path): {diameter4}, Path: {path}")
print(f"Diameter (with nodes): {diameter5}, Max path: {max_path}")
print(f"Diameter (with validation): {diameter6}")
print(f"Diameter (with level): {diameter7}")
print(f"Diameter (with count): {diameter8}")
print(f"Diameter (with odd/even): {diameter9}")
print(f"Diameter (with positive/negative): {diameter10}")
print(f"Diameter (with range 1-5): {diameter11}")
