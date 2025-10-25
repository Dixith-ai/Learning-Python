class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_middle_element(head):
    if not head:
        return None
    
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

def find_middle_element_count(head):
    if not head:
        return None
    
    count = 0
    current = head
    
    while current:
        count += 1
        current = current.next
    
    middle = count // 2
    current = head
    
    for _ in range(middle):
        current = current.next
    
    return current

def find_middle_element_stack(head):
    if not head:
        return None
    
    stack = []
    current = head
    
    while current:
        stack.append(current)
        current = current.next
    
    return stack[len(stack) // 2]

def find_middle_element_recursive(head):
    def helper(node, count):
        if not node:
            return None, 0
        
        result, total_count = helper(node.next, count)
        total_count += 1
        
        if total_count == count // 2:
            return node, total_count
        
        return result, total_count
    
    if not head:
        return None
    
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    
    result, _ = helper(head, count)
    return result

def find_middle_element_two_pointers(head):
    if not head:
        return None
    
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

def find_middle_element_with_prev(head):
    if not head:
        return None
    
    slow = fast = head
    prev = None
    
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    
    return slow, prev

def create_linked_list(values):
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

def print_linked_list(head):
    values = []
    current = head
    
    while current:
        values.append(current.val)
        current = current.next
    
    return values

values = [1, 2, 3, 4, 5, 6]
head = create_linked_list(values)

middle1 = find_middle_element(head)
middle2 = find_middle_element_count(head)
middle3 = find_middle_element_stack(head)
middle4 = find_middle_element_recursive(head)
middle5 = find_middle_element_two_pointers(head)
middle6, prev = find_middle_element_with_prev(head)

print(f"Linked list: {print_linked_list(head)}")
print(f"Middle element (two pointers): {middle1.val if middle1 else None}")
print(f"Middle element (count): {middle2.val if middle2 else None}")
print(f"Middle element (stack): {middle3.val if middle3 else None}")
print(f"Middle element (recursive): {middle4.val if middle4 else None}")
print(f"Middle element (two pointers): {middle5.val if middle5 else None}")
print(f"Middle element (with prev): {middle6.val if middle6 else None}")
print(f"Previous element: {prev.val if prev else None}")
