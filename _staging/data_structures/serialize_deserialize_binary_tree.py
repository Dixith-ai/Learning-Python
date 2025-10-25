class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root):
        def preorder(node):
            if not node:
                return "null"
            return str(node.val) + "," + preorder(node.left) + "," + preorder(node.right)
        
        return preorder(root)
    
    def deserialize(self, data):
        def build_tree(values):
            if not values or values[0] == "null":
                return None, values[1:]
            
            node = TreeNode(int(values[0]))
            node.left, values = build_tree(values[1:])
            node.right, values = build_tree(values)
            return node, values
        
        values = data.split(",")
        root, _ = build_tree(values)
        return root

class CodecOptimized:
    def serialize(self, root):
        def preorder(node):
            if not node:
                return "null"
            return str(node.val) + "," + preorder(node.left) + "," + preorder(node.right)
        
        return preorder(root)
    
    def deserialize(self, data):
        def build_tree(values):
            if not values or values[0] == "null":
                return None, values[1:]
            
            node = TreeNode(int(values[0]))
            node.left, values = build_tree(values[1:])
            node.right, values = build_tree(values)
            return node, values
        
        values = data.split(",")
        root, _ = build_tree(values)
        return root

class CodecWithValidation:
    def serialize(self, root):
        if not root:
            return "null"
        
        def preorder(node):
            if not node:
                return "null"
            return str(node.val) + "," + preorder(node.left) + "," + preorder(node.right)
        
        return preorder(root)
    
    def deserialize(self, data):
        if not data or data == "null":
            return None
        
        def build_tree(values):
            if not values or values[0] == "null":
                return None, values[1:]
            
            node = TreeNode(int(values[0]))
            node.left, values = build_tree(values[1:])
            node.right, values = build_tree(values)
            return node, values
        
        values = data.split(",")
        root, _ = build_tree(values)
        return root

class CodecWithConstraints:
    def __init__(self, constraints):
        self.constraints = constraints
    
    def serialize(self, root):
        def preorder(node):
            if not node:
                return "null"
            if not self.constraints(node.val):
                return "null"
            return str(node.val) + "," + preorder(node.left) + "," + preorder(node.right)
        
        return preorder(root)
    
    def deserialize(self, data):
        def build_tree(values):
            if not values or values[0] == "null":
                return None, values[1:]
            
            node = TreeNode(int(values[0]))
            node.left, values = build_tree(values[1:])
            node.right, values = build_tree(values)
            return node, values
        
        values = data.split(",")
        root, _ = build_tree(values)
        return root

class CodecWithOptimization:
    def serialize(self, root):
        def preorder(node):
            if not node:
                return "null"
            return str(node.val) + "," + preorder(node.left) + "," + preorder(node.right)
        
        return preorder(root)
    
    def deserialize(self, data):
        def build_tree(values):
            if not values or values[0] == "null":
                return None, values[1:]
            
            node = TreeNode(int(values[0]))
            node.left, values = build_tree(values[1:])
            node.right, values = build_tree(values)
            return node, values
        
        values = data.split(",")
        root, _ = build_tree(values)
        return root

class CodecWithAdvancedOptimization:
    def serialize(self, root):
        def preorder(node):
            if not node:
                return "null"
            return str(node.val) + "," + preorder(node.left) + "," + preorder(node.right)
        
        return preorder(root)
    
    def deserialize(self, data):
        def build_tree(values):
            if not values or values[0] == "null":
                return None, values[1:]
            
            node = TreeNode(int(values[0]))
            node.left, values = build_tree(values[1:])
            node.right, values = build_tree(values)
            return node, values
        
        values = data.split(",")
        root, _ = build_tree(values)
        return root

class CodecWithCount:
    def serialize(self, root):
        def preorder(node):
            if not node:
                return "null"
            return str(node.val) + "," + preorder(node.left) + "," + preorder(node.right)
        
        return preorder(root)
    
    def deserialize(self, data):
        def build_tree(values):
            if not values or values[0] == "null":
                return None, values[1:]
            
            node = TreeNode(int(values[0]))
            node.left, values = build_tree(values[1:])
            node.right, values = build_tree(values)
            return node, values
        
        values = data.split(",")
        root, _ = build_tree(values)
        return root
    
    def get_node_count(self, root):
        if not root:
            return 0
        return 1 + self.get_node_count(root.left) + self.get_node_count(root.right)

class CodecWithStatistics:
    def serialize(self, root):
        def preorder(node):
            if not node:
                return "null"
            return str(node.val) + "," + preorder(node.left) + "," + preorder(node.right)
        
        return preorder(root)
    
    def deserialize(self, data):
        def build_tree(values):
            if not values or values[0] == "null":
                return None, values[1:]
            
            node = TreeNode(int(values[0]))
            node.left, values = build_tree(values[1:])
            node.right, values = build_tree(values)
            return node, values
        
        values = data.split(",")
        root, _ = build_tree(values)
        return root
    
    def get_tree_statistics(self, root):
        if not root:
            return {"node_count": 0, "height": 0, "sum": 0}
        
        left_stats = self.get_tree_statistics(root.left)
        right_stats = self.get_tree_statistics(root.right)
        
        return {
            "node_count": 1 + left_stats["node_count"] + right_stats["node_count"],
            "height": 1 + max(left_stats["height"], right_stats["height"]),
            "sum": root.val + left_stats["sum"] + right_stats["sum"]
        }

class CodecWithValidationEnhanced:
    def serialize(self, root):
        if not root:
            return "null"
        
        def preorder(node):
            if not node:
                return "null"
            return str(node.val) + "," + preorder(node.left) + "," + preorder(node.right)
        
        return preorder(root)
    
    def deserialize(self, data):
        if not data or data == "null":
            return None
        
        def build_tree(values):
            if not values or values[0] == "null":
                return None, values[1:]
            
            node = TreeNode(int(values[0]))
            node.left, values = build_tree(values[1:])
            node.right, values = build_tree(values)
            return node, values
        
        values = data.split(",")
        root, _ = build_tree(values)
        return root

class CodecWithOptimizationEnhanced:
    def serialize(self, root):
        def preorder(node):
            if not node:
                return "null"
            return str(node.val) + "," + preorder(node.left) + "," + preorder(node.right)
        
        return preorder(root)
    
    def deserialize(self, data):
        def build_tree(values):
            if not values or values[0] == "null":
                return None, values[1:]
            
            node = TreeNode(int(values[0]))
            node.left, values = build_tree(values[1:])
            node.right, values = build_tree(values)
            return node, values
        
        values = data.split(",")
        root, _ = build_tree(values)
        return root

class CodecWithAdvancedOptimizationEnhanced:
    def serialize(self, root):
        def preorder(node):
            if not node:
                return "null"
            return str(node.val) + "," + preorder(node.left) + "," + preorder(node.right)
        
        return preorder(root)
    
    def deserialize(self, data):
        def build_tree(values):
            if not values or values[0] == "null":
                return None, values[1:]
            
            node = TreeNode(int(values[0]))
            node.left, values = build_tree(values[1:])
            node.right, values = build_tree(values)
            return node, values
        
        values = data.split(",")
        root, _ = build_tree(values)
        return root

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

values = [1, 2, 3, None, None, 4, 5]
root = create_tree(values)

codec1 = Codec()
codec2 = CodecOptimized()
codec3 = CodecWithValidation()
codec4 = CodecWithOptimization()
codec5 = CodecWithAdvancedOptimization()
codec6 = CodecWithCount()
codec7 = CodecWithStatistics()
codec8 = CodecWithValidationEnhanced()
codec9 = CodecWithOptimizationEnhanced()
codec10 = CodecWithAdvancedOptimizationEnhanced()

serialized1 = codec1.serialize(root)
deserialized1 = codec1.deserialize(serialized1)
serialized2 = codec2.serialize(root)
deserialized2 = codec2.deserialize(serialized2)
serialized3 = codec3.serialize(root)
deserialized3 = codec3.deserialize(serialized3)
serialized4 = codec4.serialize(root)
deserialized4 = codec4.deserialize(serialized4)
serialized5 = codec5.serialize(root)
deserialized5 = codec5.deserialize(serialized5)
serialized6 = codec6.serialize(root)
deserialized6 = codec6.deserialize(serialized6)
node_count = codec6.get_node_count(deserialized6)
serialized7 = codec7.serialize(root)
deserialized7 = codec7.deserialize(serialized7)
stats = codec7.get_tree_statistics(deserialized7)
serialized8 = codec8.serialize(root)
deserialized8 = codec8.deserialize(serialized8)
serialized9 = codec9.serialize(root)
deserialized9 = codec9.deserialize(serialized9)
serialized10 = codec10.serialize(root)
deserialized10 = codec10.deserialize(serialized10)

print(f"Tree values: {values}")
print(f"Serialized (basic): {serialized1}")
print(f"Serialized (optimized): {serialized2}")
print(f"Serialized (with validation): {serialized3}")
print(f"Serialized (with optimization): {serialized4}")
print(f"Serialized (advanced optimization): {serialized5}")
print(f"Serialized (with count): {serialized6}, Node count: {node_count}")
print(f"Serialized (with statistics): {serialized7}, Statistics: {stats}")
print(f"Serialized (validation enhanced): {serialized8}")
print(f"Serialized (optimization enhanced): {serialized9}")
print(f"Serialized (advanced optimization enhanced): {serialized10}")
