class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        self.root = self._insert_recursive(self.root, val)
    
    def _insert_recursive(self, node, val):
        if not node:
            return TreeNode(val)
        
        if val < node.val:
            node.left = self._insert_recursive(node.left, val)
        elif val > node.val:
            node.right = self._insert_recursive(node.right, val)
        
        return node
    
    def insert_iterative(self, val):
        if not self.root:
            self.root = TreeNode(val)
            return
        
        current = self.root
        while True:
            if val < current.val:
                if not current.left:
                    current.left = TreeNode(val)
                    break
                current = current.left
            elif val > current.val:
                if not current.right:
                    current.right = TreeNode(val)
                    break
                current = current.right
            else:
                break
    
    def search(self, val):
        return self._search_recursive(self.root, val)
    
    def _search_recursive(self, node, val):
        if not node or node.val == val:
            return node
        
        if val < node.val:
            return self._search_recursive(node.left, val)
        else:
            return self._search_recursive(node.right, val)
    
    def search_iterative(self, val):
        current = self.root
        
        while current:
            if current.val == val:
                return current
            elif val < current.val:
                current = current.left
            else:
                current = current.right
        
        return None
    
    def delete(self, val):
        self.root = self._delete_recursive(self.root, val)
    
    def _delete_recursive(self, node, val):
        if not node:
            return None
        
        if val < node.val:
            node.left = self._delete_recursive(node.left, val)
        elif val > node.val:
            node.right = self._delete_recursive(node.right, val)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            
            min_node = self._find_min(node.right)
            node.val = min_node.val
            node.right = self._delete_recursive(node.right, min_node.val)
        
        return node
    
    def _find_min(self, node):
        while node.left:
            node = node.left
        return node
    
    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.val)
            self._inorder_recursive(node.right, result)
    
    def preorder_traversal(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.val)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def postorder_traversal(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.val)
    
    def level_order_traversal(self):
        if not self.root:
            return []
        
        result = []
        queue = [self.root]
        
        while queue:
            node = queue.pop(0)
            result.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return result
    
    def height(self):
        return self._height_recursive(self.root)
    
    def _height_recursive(self, node):
        if not node:
            return 0
        
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        
        return 1 + max(left_height, right_height)
    
    def size(self):
        return self._size_recursive(self.root)
    
    def _size_recursive(self, node):
        if not node:
            return 0
        
        return 1 + self._size_recursive(node.left) + self._size_recursive(node.right)
    
    def is_valid_bst(self):
        return self._is_valid_bst_recursive(self.root, float('-inf'), float('inf'))
    
    def _is_valid_bst_recursive(self, node, min_val, max_val):
        if not node:
            return True
        
        if node.val <= min_val or node.val >= max_val:
            return False
        
        return (self._is_valid_bst_recursive(node.left, min_val, node.val) and
                self._is_valid_bst_recursive(node.right, node.val, max_val))
    
    def find_min(self):
        if not self.root:
            return None
        
        current = self.root
        while current.left:
            current = current.left
        
        return current.val
    
    def find_max(self):
        if not self.root:
            return None
        
        current = self.root
        while current.right:
            current = current.right
        
        return current.val
    
    def successor(self, val):
        node = self.search(val)
        if not node:
            return None
        
        if node.right:
            current = node.right
            while current.left:
                current = current.left
            return current.val
        
        successor = None
        current = self.root
        
        while current:
            if val < current.val:
                successor = current
                current = current.left
            elif val > current.val:
                current = current.right
            else:
                break
        
        return successor.val if successor else None
    
    def predecessor(self, val):
        node = self.search(val)
        if not node:
            return None
        
        if node.left:
            current = node.left
            while current.right:
                current = current.right
            return current.val
        
        predecessor = None
        current = self.root
        
        while current:
            if val > current.val:
                predecessor = current
                current = current.right
            elif val < current.val:
                current = current.left
            else:
                break
        
        return predecessor.val if predecessor else None

bst = BST()
values = [5, 3, 7, 1, 4, 6, 8]

for val in values:
    bst.insert(val)

print(f"BST values: {values}")
print(f"Inorder traversal: {bst.inorder_traversal()}")
print(f"Preorder traversal: {bst.preorder_traversal()}")
print(f"Postorder traversal: {bst.postorder_traversal()}")
print(f"Level order traversal: {bst.level_order_traversal()}")
print(f"Height: {bst.height()}")
print(f"Size: {bst.size()}")
print(f"Is valid BST: {bst.is_valid_bst()}")
print(f"Minimum value: {bst.find_min()}")
print(f"Maximum value: {bst.find_max()}")
print(f"Successor of 4: {bst.successor(4)}")
print(f"Predecessor of 6: {bst.predecessor(6)}")

bst.delete(3)
print(f"After deleting 3: {bst.inorder_traversal()}")
