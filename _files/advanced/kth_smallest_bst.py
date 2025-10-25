class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kth_smallest_inorder(root, k):
    def inorder_traversal(node):
        if not node:
            return []
        
        result = []
        result.extend(inorder_traversal(node.left))
        result.append(node.val)
        result.extend(inorder_traversal(node.right))
        return result
    
    values = inorder_traversal(root)
    return values[k - 1] if k <= len(values) else None

def kth_smallest_iterative(root, k):
    stack = []
    current = root
    
    while True:
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        k -= 1
        
        if k == 0:
            return current.val
        
        current = current.right

def kth_smallest_recursive(root, k):
    def inorder_count(node):
        if not node:
            return 0
        
        left_count = inorder_count(node.left)
        
        if left_count == k - 1:
            return node.val
        
        if left_count >= k:
            return inorder_count(node.left)
        else:
            return inorder_count(node.right)
    
    return inorder_count(root)

def kth_smallest_with_count(root, k):
    def count_nodes(node):
        if not node:
            return 0
        
        return 1 + count_nodes(node.left) + count_nodes(node.right)
    
    def find_kth(node, k):
        if not node:
            return None
        
        left_count = count_nodes(node.left)
        
        if left_count == k - 1:
            return node.val
        elif left_count >= k:
            return find_kth(node.left, k)
        else:
            return find_kth(node.right, k - left_count - 1)
    
    return find_kth(root, k)

def kth_smallest_optimized(root, k):
    stack = []
    current = root
    
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        k -= 1
        
        if k == 0:
            return current.val
        
        current = current.right
    
    return None

def kth_smallest_morris(root, k):
    current = root
    
    while current:
        if not current.left:
            k -= 1
            if k == 0:
                return current.val
            current = current.right
        else:
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right
            
            if not predecessor.right:
                predecessor.right = current
                current = current.left
            else:
                predecessor.right = None
                k -= 1
                if k == 0:
                    return current.val
                current = current.right
    
    return None

def kth_smallest_with_validation(root, k):
    if not root or k <= 0:
        return None
    
    def count_nodes(node):
        if not node:
            return 0
        return 1 + count_nodes(node.left) + count_nodes(node.right)
    
    total_nodes = count_nodes(root)
    if k > total_nodes:
        return None
    
    stack = []
    current = root
    
    while True:
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        k -= 1
        
        if k == 0:
            return current.val
        
        current = current.right

def kth_smallest_reverse_inorder(root, k):
    def reverse_inorder(node):
        if not node:
            return []
        
        result = []
        result.extend(reverse_inorder(node.right))
        result.append(node.val)
        result.extend(reverse_inorder(node.left))
        return result
    
    values = reverse_inorder(root)
    return values[k - 1] if k <= len(values) else None

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

values = [5, 3, 7, 1, 4, 6, 8]
root = create_bst(values)
k = 3

kth1 = kth_smallest_inorder(root, k)
kth2 = kth_smallest_iterative(root, k)
kth3 = kth_smallest_recursive(root, k)
kth4 = kth_smallest_with_count(root, k)
kth5 = kth_smallest_optimized(root, k)
kth6 = kth_smallest_morris(root, k)
kth7 = kth_smallest_with_validation(root, k)
kth8 = kth_smallest_reverse_inorder(root, k)

print(f"BST values: {values}")
print(f"Inorder traversal: {inorder_traversal(root)}")
print(f"{k}th smallest (inorder): {kth1}")
print(f"{k}th smallest (iterative): {kth2}")
print(f"{k}th smallest (recursive): {kth3}")
print(f"{k}th smallest (with count): {kth4}")
print(f"{k}th smallest (optimized): {kth5}")
print(f"{k}th smallest (Morris): {kth6}")
print(f"{k}th smallest (validation): {kth7}")
print(f"{k}th smallest (reverse inorder): {kth8}")
