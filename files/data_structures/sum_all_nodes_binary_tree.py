class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sum_all_nodes_recursive(root):
    if not root:
        return 0
    
    return root.val + sum_all_nodes_recursive(root.left) + sum_all_nodes_recursive(root.right)

def sum_all_nodes_iterative(root):
    if not root:
        return 0
    
    total = 0
    stack = [root]
    
    while stack:
        node = stack.pop()
        total += node.val
        
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return total

def sum_all_nodes_level_order(root):
    if not root:
        return 0
    
    total = 0
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        total += node.val
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return total

def sum_all_nodes_inorder(root):
    if not root:
        return 0
    
    total = 0
    stack = []
    current = root
    
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        total += current.val
        current = current.right
    
    return total

def sum_all_nodes_preorder(root):
    if not root:
        return 0
    
    total = 0
    stack = [root]
    
    while stack:
        node = stack.pop()
        total += node.val
        
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return total

def sum_all_nodes_postorder(root):
    if not root:
        return 0
    
    total = 0
    stack = []
    current = root
    last_visited = None
    
    while current or stack:
        if current:
            stack.append(current)
            current = current.left
        else:
            peek = stack[-1]
            if peek.right and last_visited != peek.right:
                current = peek.right
            else:
                total += peek.val
                last_visited = stack.pop()
    
    return total

def sum_all_nodes_with_validation(root):
    if not root:
        return 0
    
    def sum_nodes(node):
        if not node:
            return 0
        
        return node.val + sum_nodes(node.left) + sum_nodes(node.right)
    
    return sum_nodes(root)

def sum_all_nodes_with_count(root):
    if not root:
        return 0
    
    def count_and_sum(node):
        if not node:
            return 0, 0
        
        left_count, left_sum = count_and_sum(node.left)
        right_count, right_sum = count_and_sum(node.right)
        
        total_count = 1 + left_count + right_count
        total_sum = node.val + left_sum + right_sum
        
        return total_count, total_sum
    
    count, total_sum = count_and_sum(root)
    return total_sum

def sum_all_nodes_with_level_sum(root):
    if not root:
        return 0
    
    level_sums = {}
    
    def dfs(node, level):
        if not node:
            return
        
        level_sums[level] = level_sums.get(level, 0) + node.val
        
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)
    
    dfs(root, 0)
    return sum(level_sums.values())

def sum_all_nodes_with_odd_even(root):
    if not root:
        return 0
    
    odd_sum = 0
    even_sum = 0
    
    def dfs(node, level):
        nonlocal odd_sum, even_sum
        
        if not node:
            return
        
        if level % 2 == 0:
            even_sum += node.val
        else:
            odd_sum += node.val
        
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)
    
    dfs(root, 0)
    return odd_sum + even_sum

def sum_all_nodes_with_positive_negative(root):
    if not root:
        return 0
    
    positive_sum = 0
    negative_sum = 0
    
    def dfs(node):
        nonlocal positive_sum, negative_sum
        
        if not node:
            return
        
        if node.val >= 0:
            positive_sum += node.val
        else:
            negative_sum += node.val
        
        dfs(node.left)
        dfs(node.right)
    
    dfs(root)
    return positive_sum + negative_sum

def sum_all_nodes_with_range(root, min_val, max_val):
    if not root:
        return 0
    
    total = 0
    
    def dfs(node):
        nonlocal total
        
        if not node:
            return
        
        if min_val <= node.val <= max_val:
            total += node.val
        
        dfs(node.left)
        dfs(node.right)
    
    dfs(root)
    return total

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

sum1 = sum_all_nodes_recursive(root)
sum2 = sum_all_nodes_iterative(root)
sum3 = sum_all_nodes_level_order(root)
sum4 = sum_all_nodes_inorder(root)
sum5 = sum_all_nodes_preorder(root)
sum6 = sum_all_nodes_postorder(root)
sum7 = sum_all_nodes_with_validation(root)
sum8 = sum_all_nodes_with_count(root)
sum9 = sum_all_nodes_with_level_sum(root)
sum10 = sum_all_nodes_with_odd_even(root)
sum11 = sum_all_nodes_with_positive_negative(root)
sum12 = sum_all_nodes_with_range(root, 1, 5)

print(f"Binary tree values: {values}")
print(f"Inorder traversal: {inorder_traversal(root)}")
print(f"Sum (recursive): {sum1}")
print(f"Sum (iterative): {sum2}")
print(f"Sum (level order): {sum3}")
print(f"Sum (inorder): {sum4}")
print(f"Sum (preorder): {sum5}")
print(f"Sum (postorder): {sum6}")
print(f"Sum (with validation): {sum7}")
print(f"Sum (with count): {sum8}")
print(f"Sum (with level sum): {sum9}")
print(f"Sum (with odd/even): {sum10}")
print(f"Sum (with positive/negative): {sum11}")
print(f"Sum (with range 1-5): {sum12}")
