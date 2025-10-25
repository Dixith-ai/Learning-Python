class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_nth_from_end_two_pointers(head, n):
    if not head:
        return None
    
    first = second = head
    
    for _ in range(n):
        if not first:
            return None
        first = first.next
    
    while first:
        first = first.next
        second = second.next
    
    return second

def find_nth_from_end_length(head, n):
    def get_length(head):
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        return length
    
    length = get_length(head)
    
    if n > length:
        return None
    
    current = head
    for _ in range(length - n):
        current = current.next
    
    return current

def find_nth_from_end_recursive(head, n):
    def helper(node):
        if not node:
            return 0
        
        index = helper(node.next) + 1
        
        if index == n:
            return node
        
        return index
    
    result = helper(head)
    return result if isinstance(result, ListNode) else None

def find_nth_from_end_stack(head, n):
    if not head:
        return None
    
    stack = []
    current = head
    
    while current:
        stack.append(current)
        current = current.next
    
    if n > len(stack):
        return None
    
    return stack[-n]

def find_nth_from_end_hash_map(head, n):
    if not head:
        return None
    
    position_map = {}
    current = head
    position = 0
    
    while current:
        position_map[position] = current
        current = current.next
        position += 1
    
    if n > position:
        return None
    
    return position_map[position - n]

def find_nth_from_end_optimized(head, n):
    if not head or n <= 0:
        return None
    
    dummy = ListNode(0)
    dummy.next = head
    first = second = dummy
    
    for _ in range(n):
        if not first.next:
            return None
        first = first.next
    
    while first.next:
        first = first.next
        second = second.next
    
    return second.next

def find_nth_from_end_with_validation(head, n):
    if not head or n <= 0:
        return None
    
    def get_length(head):
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        return length
    
    length = get_length(head)
    
    if n > length:
        return None
    
    current = head
    for _ in range(length - n):
        current = current.next
    
    return current

def find_nth_from_end_reverse(head, n):
    def reverse_list(head):
        prev = None
        current = head
        
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        
        return prev
    
    reversed_head = reverse_list(head)
    current = reversed_head
    
    for _ in range(n - 1):
        if not current:
            return None
        current = current.next
    
    return current

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
n = 2

nth1 = find_nth_from_end_two_pointers(head, n)
nth2 = find_nth_from_end_length(create_linked_list(values), n)
nth3 = find_nth_from_end_recursive(create_linked_list(values), n)
nth4 = find_nth_from_end_stack(create_linked_list(values), n)
nth5 = find_nth_from_end_hash_map(create_linked_list(values), n)
nth6 = find_nth_from_end_optimized(create_linked_list(values), n)
nth7 = find_nth_from_end_with_validation(create_linked_list(values), n)
nth8 = find_nth_from_end_reverse(create_linked_list(values), n)

print(f"Linked list: {print_linked_list(head)}")
print(f"{n}th node from end (two pointers): {nth1.val if nth1 else None}")
print(f"{n}th node from end (length): {nth2.val if nth2 else None}")
print(f"{n}th node from end (recursive): {nth3.val if nth3 else None}")
print(f"{n}th node from end (stack): {nth4.val if nth4 else None}")
print(f"{n}th node from end (hash map): {nth5.val if nth5 else None}")
print(f"{n}th node from end (optimized): {nth6.val if nth6 else None}")
print(f"{n}th node from end (validation): {nth7.val if nth7 else None}")
print(f"{n}th node from end (reverse): {nth8.val if nth8 else None}")
