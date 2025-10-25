class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst_recursive(root):
    def validate(node, min_val, max_val):
        if not node:
            return True
        
        if node.val <= min_val or node.val >= max_val:
            return False
        
        return (validate(node.left, min_val, node.val) and
                validate(node.right, node.val, max_val))
    
    return validate(root, float('-inf'), float('inf'))

def is_valid_bst_inorder(root):
    def inorder_traversal(node):
        if not node:
            return []
        
        result = []
        result.extend(inorder_traversal(node.left))
        result.append(node.val)
        result.extend(inorder_traversal(node.right))
        return result
    
    values = inorder_traversal(root)
    
    for i in range(1, len(values)):
        if values[i] <= values[i - 1]:
            return False
    
    return True

def is_valid_bst_iterative(root):
    if not root:
        return True
    
    stack = []
    current = root
    prev = None
    
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        
        if prev and current.val <= prev.val:
            return False
        
        prev = current
        current = current.right
    
    return True

def is_valid_bst_with_validation(root):
    if not root:
        return True
    
    def validate_with_bounds(node, min_val, max_val):
        if not node:
            return True
        
        if node.val < min_val or node.val > max_val:
            return False
        
        return (validate_with_bounds(node.left, min_val, node.val - 1) and
                validate_with_bounds(node.right, node.val + 1, max_val))
    
    return validate_with_bounds(root, float('-inf'), float('inf'))

def is_valid_bst_with_count(root):
    def count_nodes(node):
        if not node:
            return 0
        return 1 + count_nodes(node.left) + count_nodes(node.right)
    
    def is_bst_with_count(node, min_val, max_val):
        if not node:
            return True
        
        if node.val < min_val or node.val > max_val:
            return False
        
        return (is_bst_with_count(node.left, min_val, node.val - 1) and
                is_bst_with_count(node.right, node.val + 1, max_val))
    
    return is_bst_with_count(root, float('-inf'), float('inf'))

def is_valid_bst_with_range(root):
    def validate_range(node, min_val, max_val):
        if not node:
            return True
        
        if node.val <= min_val or node.val >= max_val:
            return False
        
        return (validate_range(node.left, min_val, node.val) and
                validate_range(node.right, node.val, max_val))
    
    return validate_range(root, float('-inf'), float('inf'))

def is_valid_bst_with_parent_pointer(root):
    def validate_with_parent(node, min_val, max_val):
        if not node:
            return True
        
        if node.val <= min_val or node.val >= max_val:
            return False
        
        return (validate_with_parent(node.left, min_val, node.val) and
                validate_with_parent(node.right, node.val, max_val))
    
    return validate_with_parent(root, float('-inf'), float('inf'))

def is_valid_bst_with_duplicates(root):
    def validate_with_duplicates(node, min_val, max_val):
        if not node:
            return True
        
        if node.val < min_val or node.val > max_val:
            return False
        
        return (validate_with_duplicates(node.left, min_val, node.val) and
                validate_with_duplicates(node.right, node.val, max_val))
    
    return validate_with_duplicates(root, float('-inf'), float('inf'))

def is_valid_bst_with_validation_enhanced(root):
    if not root:
        return True
    
    def validate_enhanced(node, min_val, max_val):
        if not node:
            return True
        
        if node.val <= min_val or node.val >= max_val:
            return False
        
        return (validate_enhanced(node.left, min_val, node.val) and
                validate_enhanced(node.right, node.val, max_val))
    
    return validate_enhanced(root, float('-inf'), float('inf'))

def is_valid_bst_with_level_validation(root):
    if not root:
        return True
    
    def validate_level(node, min_val, max_val, level):
        if not node:
            return True
        
        if node.val <= min_val or node.val >= max_val:
            return False
        
        return (validate_level(node.left, min_val, node.val, level + 1) and
                validate_level(node.right, node.val, max_val, level + 1))
    
    return validate_level(root, float('-inf'), float('inf'), 0)

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

def create_invalid_bst():
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    return root

def inorder_traversal(root):
    if not root:
        return []
    
    result = []
    result.extend(inorder_traversal(root.left))
    result.append(root.val)
    result.extend(inorder_traversal(root.right))
    return result

valid_values = [5, 3, 7, 1, 4, 6, 8]
valid_root = create_bst(valid_values)
invalid_root = create_invalid_bst()

print(f"Valid BST values: {valid_values}")
print(f"Valid BST inorder: {inorder_traversal(valid_root)}")
print(f"Is valid BST (recursive): {is_valid_bst_recursive(valid_root)}")
print(f"Is valid BST (inorder): {is_valid_bst_inorder(valid_root)}")
print(f"Is valid BST (iterative): {is_valid_bst_iterative(valid_root)}")
print(f"Is valid BST (with validation): {is_valid_bst_with_validation(valid_root)}")
print(f"Is valid BST (with count): {is_valid_bst_with_count(valid_root)}")
print(f"Is valid BST (with range): {is_valid_bst_with_range(valid_root)}")
print(f"Is valid BST (with parent): {is_valid_bst_with_parent_pointer(valid_root)}")
print(f"Is valid BST (with duplicates): {is_valid_bst_with_duplicates(valid_root)}")
print(f"Is valid BST (enhanced): {is_valid_bst_with_validation_enhanced(valid_root)}")
print(f"Is valid BST (level validation): {is_valid_bst_with_level_validation(valid_root)}")

print(f"\nInvalid BST inorder: {inorder_traversal(invalid_root)}")
print(f"Is invalid BST (recursive): {is_valid_bst_recursive(invalid_root)}")
print(f"Is invalid BST (inorder): {is_valid_bst_inorder(invalid_root)}")
print(f"Is invalid BST (iterative): {is_valid_bst_iterative(invalid_root)}")
print(f"Is invalid BST (with validation): {is_valid_bst_with_validation(invalid_root)}")
print(f"Is invalid BST (with count): {is_valid_bst_with_count(invalid_root)}")
print(f"Is invalid BST (with range): {is_valid_bst_with_range(invalid_root)}")
print(f"Is invalid BST (with parent): {is_valid_bst_with_parent_pointer(invalid_root)}")
print(f"Is invalid BST (with duplicates): {is_valid_bst_with_duplicates(invalid_root)}")
print(f"Is invalid BST (enhanced): {is_valid_bst_with_validation_enhanced(invalid_root)}")
print(f"Is invalid BST (level validation): {is_valid_bst_with_level_validation(invalid_root)}")
