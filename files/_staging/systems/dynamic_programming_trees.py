class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def house_robber_tree_recursive(root):
    def helper(node):
        if not node:
            return 0, 0
        
        left_rob, left_not_rob = helper(node.left)
        right_rob, right_not_rob = helper(node.right)
        
        rob = node.val + left_not_rob + right_not_rob
        not_rob = max(left_rob, left_not_rob) + max(right_rob, right_not_rob)
        
        return rob, not_rob
    
    rob, not_rob = helper(root)
    return max(rob, not_rob)

def house_robber_tree_memoization(root):
    memo = {}
    
    def helper(node):
        if node in memo:
            return memo[node]
        
        if not node:
            return 0, 0
        
        left_rob, left_not_rob = helper(node.left)
        right_rob, right_not_rob = helper(node.right)
        
        rob = node.val + left_not_rob + right_not_rob
        not_rob = max(left_rob, left_not_rob) + max(right_rob, right_not_rob)
        
        memo[node] = (rob, not_rob)
        return rob, not_rob
    
    rob, not_rob = helper(root)
    return max(rob, not_rob)

def house_robber_tree_dp(root):
    def helper(node):
        if not node:
            return 0, 0
        
        left_rob, left_not_rob = helper(node.left)
        right_rob, right_not_rob = helper(node.right)
        
        rob = node.val + left_not_rob + right_not_rob
        not_rob = max(left_rob, left_not_rob) + max(right_rob, right_not_rob)
        
        return rob, not_rob
    
    rob, not_rob = helper(root)
    return max(rob, not_rob)

def house_robber_tree_with_validation(root):
    if not root:
        return 0
    
    def helper(node):
        if not node:
            return 0, 0
        
        left_rob, left_not_rob = helper(node.left)
        right_rob, right_not_rob = helper(node.right)
        
        rob = node.val + left_not_rob + right_not_rob
        not_rob = max(left_rob, left_not_rob) + max(right_rob, right_not_rob)
        
        return rob, not_rob
    
    rob, not_rob = helper(root)
    return max(rob, not_rob)

def house_robber_tree_with_constraints(root, constraints):
    def helper(node):
        if not node:
            return 0, 0
        
        left_rob, left_not_rob = helper(node.left)
        right_rob, right_not_rob = helper(node.right)
        
        if constraints(node):
            rob = node.val + left_not_rob + right_not_rob
        else:
            rob = 0
        
        not_rob = max(left_rob, left_not_rob) + max(right_rob, right_not_rob)
        
        return rob, not_rob
    
    rob, not_rob = helper(root)
    return max(rob, not_rob)

def house_robber_tree_with_optimization(root):
    def helper(node):
        if not node:
            return 0, 0
        
        left_rob, left_not_rob = helper(node.left)
        right_rob, right_not_rob = helper(node.right)
        
        rob = node.val + left_not_rob + right_not_rob
        not_rob = max(left_rob, left_not_rob) + max(right_rob, right_not_rob)
        
        return rob, not_rob
    
    rob, not_rob = helper(root)
    return max(rob, not_rob)

def house_robber_tree_with_advanced_optimization(root):
    def helper(node):
        if not node:
            return 0, 0
        
        left_rob, left_not_rob = helper(node.left)
        right_rob, right_not_rob = helper(node.right)
        
        rob = node.val + left_not_rob + right_not_rob
        not_rob = max(left_rob, left_not_rob) + max(right_rob, right_not_rob)
        
        return rob, not_rob
    
    rob, not_rob = helper(root)
    return max(rob, not_rob)

def house_robber_tree_with_count(root):
    def helper(node):
        if not node:
            return 0, 0, 0, 0
        
        left_rob, left_not_rob, left_rob_count, left_not_rob_count = helper(node.left)
        right_rob, right_not_rob, right_rob_count, right_not_rob_count = helper(node.right)
        
        rob = node.val + left_not_rob + right_not_rob
        rob_count = left_not_rob_count + right_not_rob_count + 1
        
        not_rob = max(left_rob, left_not_rob) + max(right_rob, right_not_rob)
        not_rob_count = (left_rob_count if left_rob > left_not_rob else left_not_rob_count) + \
                       (right_rob_count if right_rob > right_not_rob else right_not_rob_count)
        
        return rob, not_rob, rob_count, not_rob_count
    
    rob, not_rob, rob_count, not_rob_count = helper(root)
    return max(rob, not_rob), (rob_count if rob > not_rob else not_rob_count)

def house_robber_tree_with_path(root):
    def helper(node):
        if not node:
            return 0, 0, [], []
        
        left_rob, left_not_rob, left_rob_path, left_not_rob_path = helper(node.left)
        right_rob, right_not_rob, right_rob_path, right_not_rob_path = helper(node.right)
        
        rob = node.val + left_not_rob + right_not_rob
        rob_path = [node.val] + left_not_rob_path + right_not_rob_path
        
        not_rob = max(left_rob, left_not_rob) + max(right_rob, right_not_rob)
        not_rob_path = (left_rob_path if left_rob > left_not_rob else left_not_rob_path) + \
                      (right_rob_path if right_rob > right_not_rob else right_not_rob_path)
        
        return rob, not_rob, rob_path, not_rob_path
    
    rob, not_rob, rob_path, not_rob_path = helper(root)
    return max(rob, not_rob), (rob_path if rob > not_rob else not_rob_path)

def house_robber_tree_with_negative(root):
    def helper(node):
        if not node:
            return 0, 0
        
        left_rob, left_not_rob = helper(node.left)
        right_rob, right_not_rob = helper(node.right)
        
        rob = max(0, node.val) + left_not_rob + right_not_rob
        not_rob = max(left_rob, left_not_rob) + max(right_rob, right_not_rob)
        
        return rob, not_rob
    
    rob, not_rob = helper(root)
    return max(rob, not_rob)

def create_tree(values):
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

values = [3, 2, 3, None, 3, None, 1]
root = create_tree(values)

robber1 = house_robber_tree_recursive(root)
robber2 = house_robber_tree_memoization(root)
robber3 = house_robber_tree_dp(root)
robber4 = house_robber_tree_with_validation(root)
robber5 = house_robber_tree_with_optimization(root)
robber6 = house_robber_tree_with_advanced_optimization(root)
robber7, count = house_robber_tree_with_count(root)
robber8, path = house_robber_tree_with_path(root)
robber9 = house_robber_tree_with_negative(root)

print(f"Tree values: {values}")
print(f"House robber (recursive): {robber1}")
print(f"House robber (memoization): {robber2}")
print(f"House robber (DP): {robber3}")
print(f"House robber (with validation): {robber4}")
print(f"House robber (with optimization): {robber5}")
print(f"House robber (advanced optimization): {robber6}")
print(f"House robber (with count): {robber7}, Count: {count}")
print(f"House robber (with path): {robber8}, Path: {path}")
print(f"House robber (with negative): {robber9}")
