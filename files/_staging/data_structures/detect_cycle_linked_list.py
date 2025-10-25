class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def detect_cycle_floyd(head):
    if not head or not head.next:
        return None
    
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            break
    
    if not fast or not fast.next:
        return None
    
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow

def detect_cycle_hash_set(head):
    visited = set()
    current = head
    
    while current:
        if current in visited:
            return current
        visited.add(current)
        current = current.next
    
    return None

def detect_cycle_visited_flag(head):
    current = head
    
    while current:
        if hasattr(current, 'visited') and current.visited:
            return current
        
        current.visited = True
        current = current.next
    
    return None

def detect_cycle_brute_force(head):
    current = head
    position = 0
    
    while current:
        temp = head
        temp_pos = 0
        
        while temp != current:
            temp = temp.next
            temp_pos += 1
        
        if temp_pos < position:
            return current
        
        current = current.next
        position += 1
    
    return None

def detect_cycle_length(head):
    if not head or not head.next:
        return 0
    
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            break
    
    if not fast or not fast.next:
        return 0
    
    length = 1
    temp = slow.next
    
    while temp != slow:
        temp = temp.next
        length += 1
    
    return length

def detect_cycle_start_position(head):
    if not head or not head.next:
        return None
    
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            break
    
    if not fast or not fast.next:
        return None
    
    slow = head
    position = 0
    
    while slow != fast:
        slow = slow.next
        fast = fast.next
        position += 1
    
    return position

def create_linked_list_with_cycle(values, cycle_pos):
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    cycle_node = None
    
    for i, val in enumerate(values[1:], 1):
        current.next = ListNode(val)
        current = current.next
        
        if i == cycle_pos:
            cycle_node = current
    
    if cycle_node:
        current.next = cycle_node
    
    return head

def print_linked_list_with_cycle(head, max_nodes=10):
    values = []
    current = head
    count = 0
    
    while current and count < max_nodes:
        values.append(current.val)
        current = current.next
        count += 1
    
    return values

values = [1, 2, 3, 4, 5, 6]
head_with_cycle = create_linked_list_with_cycle(values, 2)
head_without_cycle = create_linked_list_with_cycle(values, -1)

cycle1 = detect_cycle_floyd(head_with_cycle)
cycle2 = detect_cycle_hash_set(head_with_cycle)
cycle3 = detect_cycle_visited_flag(head_with_cycle)
cycle4 = detect_cycle_brute_force(head_with_cycle)

cycle_length = detect_cycle_length(head_with_cycle)
cycle_position = detect_cycle_start_position(head_with_cycle)

print(f"Linked list with cycle: {print_linked_list_with_cycle(head_with_cycle)}")
print(f"Cycle detected (Floyd): {cycle1.val if cycle1 else None}")
print(f"Cycle detected (HashSet): {cycle2.val if cycle2 else None}")
print(f"Cycle detected (Flag): {cycle3.val if cycle3 else None}")
print(f"Cycle detected (Brute force): {cycle4.val if cycle4 else None}")
print(f"Cycle length: {cycle_length}")
print(f"Cycle start position: {cycle_position}")

no_cycle = detect_cycle_floyd(head_without_cycle)
print(f"No cycle detected: {no_cycle}")
