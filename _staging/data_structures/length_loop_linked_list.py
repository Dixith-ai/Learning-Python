class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_loop_length_floyd(head):
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

def find_loop_length_hash_set(head):
    visited = {}
    current = head
    position = 0
    
    while current:
        if current in visited:
            return position - visited[current]
        
        visited[current] = position
        current = current.next
        position += 1
    
    return 0

def find_loop_length_visited_flag(head):
    current = head
    position = 0
    
    while current:
        if hasattr(current, 'visited') and current.visited:
            return position - current.position
        
        current.visited = True
        current.position = position
        current = current.next
        position += 1
    
    return 0

def find_loop_length_brute_force(head):
    current = head
    position = 0
    
    while current:
        temp = head
        temp_pos = 0
        
        while temp != current:
            temp = temp.next
            temp_pos += 1
        
        if temp_pos < position:
            return position - temp_pos
        
        current = current.next
        position += 1
    
    return 0

def find_loop_length_optimized(head):
    if not head or not head.next:
        return 0
    
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            length = 1
            temp = slow.next
            
            while temp != slow:
                temp = temp.next
                length += 1
            
            return length
    
    return 0

def find_loop_length_with_start(head):
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
    
    slow = head
    start_position = 0
    
    while slow != fast:
        slow = slow.next
        fast = fast.next
        start_position += 1
    
    length = 1
    temp = slow.next
    
    while temp != slow:
        temp = temp.next
        length += 1
    
    return length, start_position

def create_linked_list_with_loop(values, loop_start):
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    loop_node = None
    
    for i, val in enumerate(values[1:], 1):
        current.next = ListNode(val)
        current = current.next
        
        if i == loop_start:
            loop_node = current
    
    if loop_node:
        current.next = loop_node
    
    return head

def print_linked_list_with_loop(head, max_nodes=10):
    values = []
    current = head
    count = 0
    
    while current and count < max_nodes:
        values.append(current.val)
        current = current.next
        count += 1
    
    return values

values = [1, 2, 3, 4, 5, 6, 7, 8]
head_with_loop = create_linked_list_with_loop(values, 3)
head_without_loop = create_linked_list_with_loop(values, -1)

length1 = find_loop_length_floyd(head_with_loop)
length2 = find_loop_length_hash_set(head_with_loop)
length3 = find_loop_length_visited_flag(head_with_loop)
length4 = find_loop_length_brute_force(head_with_loop)
length5 = find_loop_length_optimized(head_with_loop)
length6, start_pos = find_loop_length_with_start(head_with_loop)

print(f"Linked list with loop: {print_linked_list_with_loop(head_with_loop)}")
print(f"Loop length (Floyd): {length1}")
print(f"Loop length (HashSet): {length2}")
print(f"Loop length (Flag): {length3}")
print(f"Loop length (Brute force): {length4}")
print(f"Loop length (Optimized): {length5}")
print(f"Loop length: {length6}, Start position: {start_pos}")

no_loop = find_loop_length_floyd(head_without_loop)
print(f"No loop detected: {no_loop}")
