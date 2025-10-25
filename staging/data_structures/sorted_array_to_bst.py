class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sorted_array_to_bst_recursive(nums):
    if not nums:
        return None
    
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sorted_array_to_bst_recursive(nums[:mid])
    root.right = sorted_array_to_bst_recursive(nums[mid + 1:])
    
    return root

def sorted_array_to_bst_iterative(nums):
    if not nums:
        return None
    
    root = TreeNode(nums[len(nums) // 2])
    stack = [(root, 0, len(nums) - 1)]
    
    while stack:
        node, start, end = stack.pop()
        mid = (start + end) // 2
        
        if start < mid:
            left_mid = (start + mid - 1) // 2
            node.left = TreeNode(nums[left_mid])
            stack.append((node.left, start, mid - 1))
        
        if mid + 1 < end:
            right_mid = (mid + 1 + end) // 2
            node.right = TreeNode(nums[right_mid])
            stack.append((node.right, mid + 1, end))
    
    return root

def sorted_array_to_bst_optimized(nums):
    def build_bst(start, end):
        if start > end:
            return None
        
        mid = (start + end) // 2
        root = TreeNode(nums[mid])
        root.left = build_bst(start, mid - 1)
        root.right = build_bst(mid + 1, end)
        
        return root
    
    return build_bst(0, len(nums) - 1)

def sorted_array_to_bst_with_validation(nums):
    if not nums:
        return None
    
    if len(nums) == 1:
        return TreeNode(nums[0])
    
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    
    if mid > 0:
        root.left = sorted_array_to_bst_with_validation(nums[:mid])
    
    if mid < len(nums) - 1:
        root.right = sorted_array_to_bst_with_validation(nums[mid + 1:])
    
    return root

def sorted_array_to_bst_balanced(nums):
    if not nums:
        return None
    
    def build_balanced_bst(start, end):
        if start > end:
            return None
        
        mid = (start + end) // 2
        root = TreeNode(nums[mid])
        
        root.left = build_balanced_bst(start, mid - 1)
        root.right = build_balanced_bst(mid + 1, end)
        
        return root
    
    return build_balanced_bst(0, len(nums) - 1)

def sorted_array_to_bst_with_height_balance(nums):
    if not nums:
        return None
    
    def build_height_balanced(start, end):
        if start > end:
            return None
        
        mid = (start + end) // 2
        root = TreeNode(nums[mid])
        
        root.left = build_height_balanced(start, mid - 1)
        root.right = build_height_balanced(mid + 1, end)
        
        return root
    
    return build_height_balanced(0, len(nums) - 1)

def sorted_array_to_bst_avl_style(nums):
    if not nums:
        return None
    
    def build_avl(start, end):
        if start > end:
            return None
        
        mid = (start + end) // 2
        root = TreeNode(nums[mid])
        
        root.left = build_avl(start, mid - 1)
        root.right = build_avl(mid + 1, end)
        
        return root
    
    return build_avl(0, len(nums) - 1)

def sorted_array_to_bst_with_duplicates(nums):
    if not nums:
        return None
    
    def build_bst_with_duplicates(start, end):
        if start > end:
            return None
        
        mid = (start + end) // 2
        root = TreeNode(nums[mid])
        
        root.left = build_bst_with_duplicates(start, mid - 1)
        root.right = build_bst_with_duplicates(mid + 1, end)
        
        return root
    
    return build_bst_with_duplicates(0, len(nums) - 1)

def inorder_traversal(root):
    if not root:
        return []
    
    result = []
    result.extend(inorder_traversal(root.left))
    result.append(root.val)
    result.extend(inorder_traversal(root.right))
    return result

def preorder_traversal(root):
    if not root:
        return []
    
    result = [root.val]
    result.extend(preorder_traversal(root.left))
    result.extend(preorder_traversal(root.right))
    return result

def postorder_traversal(root):
    if not root:
        return []
    
    result = []
    result.extend(postorder_traversal(root.left))
    result.extend(postorder_traversal(root.right))
    result.append(root.val)
    return result

def level_order_traversal(root):
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        result.append(node.val)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result

def height_of_tree(root):
    if not root:
        return 0
    
    left_height = height_of_tree(root.left)
    right_height = height_of_tree(root.right)
    
    return 1 + max(left_height, right_height)

def is_balanced_bst(root):
    if not root:
        return True
    
    left_height = height_of_tree(root.left)
    right_height = height_of_tree(root.right)
    
    return (abs(left_height - right_height) <= 1 and
            is_balanced_bst(root.left) and
            is_balanced_bst(root.right))

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

root1 = sorted_array_to_bst_recursive(nums)
root2 = sorted_array_to_bst_iterative(nums)
root3 = sorted_array_to_bst_optimized(nums)
root4 = sorted_array_to_bst_with_validation(nums)
root5 = sorted_array_to_bst_balanced(nums)
root6 = sorted_array_to_bst_with_height_balance(nums)
root7 = sorted_array_to_bst_avl_style(nums)
root8 = sorted_array_to_bst_with_duplicates(nums)

print(f"Sorted array: {nums}")
print(f"Inorder traversal: {inorder_traversal(root1)}")
print(f"Preorder traversal: {preorder_traversal(root1)}")
print(f"Postorder traversal: {postorder_traversal(root1)}")
print(f"Level order traversal: {level_order_traversal(root1)}")
print(f"Height: {height_of_tree(root1)}")
print(f"Is balanced: {is_balanced_bst(root1)}")

print(f"All roots are equal: {inorder_traversal(root1) == inorder_traversal(root2) == inorder_traversal(root3)}")
