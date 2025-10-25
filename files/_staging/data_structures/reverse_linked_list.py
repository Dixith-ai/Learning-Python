class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list_iterative(head):
    prev = None
    current = head
    
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    
    return prev

def reverse_linked_list_recursive(head):
    if not head or not head.next:
        return head
    
    new_head = reverse_linked_list_recursive(head.next)
    head.next.next = head
    head.next = None
    
    return new_head

def reverse_linked_list_stack(head):
    if not head:
        return None
    
    stack = []
    current = head
    
    while current:
        stack.append(current)
        current = current.next
    
    new_head = stack.pop()
    current = new_head
    
    while stack:
        current.next = stack.pop()
        current = current.next
    
    current.next = None
    return new_head

def reverse_linked_list_inplace(head):
    if not head:
        return None
    
    prev = None
    current = head
    
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    return prev

def reverse_linked_list_partial(head, m, n):
    if not head or m == n:
        return head
    
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    
    for _ in range(m - 1):
        prev = prev.next
    
    current = prev.next
    
    for _ in range(n - m):
        next_node = current.next
        current.next = next_node.next
        next_node.next = prev.next
        prev.next = next_node
    
    return dummy.next

def reverse_linked_list_groups(head, k):
    if not head or k <= 1:
        return head
    
    current = head
    next_node = None
    prev = None
    count = 0
    
    while current and count < k:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
        count += 1
    
    if next_node:
        head.next = reverse_linked_list_groups(next_node, k)
    
    return prev

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

values = [1, 2, 3, 4, 5]
head = create_linked_list(values)

reversed1 = reverse_linked_list_iterative(head)
reversed2 = reverse_linked_list_recursive(create_linked_list(values))
reversed3 = reverse_linked_list_stack(create_linked_list(values))
reversed4 = reverse_linked_list_inplace(create_linked_list(values))

print(f"Original: {print_linked_list(create_linked_list(values))}")
print(f"Reversed (iterative): {print_linked_list(reversed1)}")
print(f"Reversed (recursive): {print_linked_list(reversed2)}")
print(f"Reversed (stack): {print_linked_list(reversed3)}")
print(f"Reversed (inplace): {print_linked_list(reversed4)}")

head_partial = create_linked_list(values)
reversed_partial = reverse_linked_list_partial(head_partial, 2, 4)
print(f"Reversed partial (2-4): {print_linked_list(reversed_partial)}")

head_groups = create_linked_list(values)
reversed_groups = reverse_linked_list_groups(head_groups, 2)
print(f"Reversed groups (k=2): {print_linked_list(reversed_groups)}")
