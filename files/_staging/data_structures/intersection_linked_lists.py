class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_intersection_hash_set(headA, headB):
    visited = set()
    current = headA
    
    while current:
        visited.add(current)
        current = current.next
    
    current = headB
    while current:
        if current in visited:
            return current
        current = current.next
    
    return None

def find_intersection_two_pointers(headA, headB):
    if not headA or not headB:
        return None
    
    pA = headA
    pB = headB
    
    while pA != pB:
        pA = headB if pA is None else pA.next
        pB = headA if pB is None else pB.next
    
    return pA

def find_intersection_length_difference(headA, headB):
    def get_length(head):
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        return length
    
    lenA = get_length(headA)
    lenB = get_length(headB)
    
    if lenA > lenB:
        for _ in range(lenA - lenB):
            headA = headA.next
    else:
        for _ in range(lenB - lenA):
            headB = headB.next
    
    while headA and headB:
        if headA == headB:
            return headA
        headA = headA.next
        headB = headB.next
    
    return None

def find_intersection_brute_force(headA, headB):
    currentA = headA
    
    while currentA:
        currentB = headB
        while currentB:
            if currentA == currentB:
                return currentA
            currentB = currentB.next
        currentA = currentA.next
    
    return None

def find_intersection_optimized(headA, headB):
    if not headA or not headB:
        return None
    
    def get_tail_and_length(head):
        length = 1
        current = head
        while current.next:
            length += 1
            current = current.next
        return current, length
    
    tailA, lenA = get_tail_and_length(headA)
    tailB, lenB = get_tail_and_length(headB)
    
    if tailA != tailB:
        return None
    
    if lenA > lenB:
        for _ in range(lenA - lenB):
            headA = headA.next
    else:
        for _ in range(lenB - lenA):
            headB = headB.next
    
    while headA != headB:
        headA = headA.next
        headB = headB.next
    
    return headA

def find_intersection_with_distance(headA, headB):
    def get_distance_to_end(head):
        distance = 0
        current = head
        while current:
            distance += 1
            current = current.next
        return distance
    
    def get_node_at_distance(head, distance):
        current = head
        for _ in range(distance):
            current = current.next
        return current
    
    distA = get_distance_to_end(headA)
    distB = get_distance_to_end(headB)
    
    if distA > distB:
        headA = get_node_at_distance(headA, distA - distB)
    else:
        headB = get_node_at_distance(headB, distB - distA)
    
    while headA and headB:
        if headA == headB:
            return headA
        headA = headA.next
        headB = headB.next
    
    return None

def create_linked_list(values):
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

def create_intersecting_lists(listA, listB, intersect_val):
    headA = create_linked_list(listA)
    headB = create_linked_list(listB)
    
    currentA = headA
    while currentA and currentA.val != intersect_val:
        currentA = currentA.next
    
    if currentA:
        currentB = headB
        while currentB.next:
            currentB = currentB.next
        currentB.next = currentA
    
    return headA, headB

def print_linked_list(head, max_nodes=10):
    values = []
    current = head
    count = 0
    
    while current and count < max_nodes:
        values.append(current.val)
        current = current.next
        count += 1
    
    return values

listA = [4, 1, 8, 4, 5]
listB = [5, 6, 1, 8, 4, 5]
headA, headB = create_intersecting_lists(listA, listB, 8)

intersection1 = find_intersection_hash_set(headA, headB)
intersection2 = find_intersection_two_pointers(headA, headB)
intersection3 = find_intersection_length_difference(headA, headB)
intersection4 = find_intersection_brute_force(headA, headB)
intersection5 = find_intersection_optimized(headA, headB)
intersection6 = find_intersection_with_distance(headA, headB)

print(f"List A: {print_linked_list(headA)}")
print(f"List B: {print_linked_list(headB)}")
print(f"Intersection (HashSet): {intersection1.val if intersection1 else None}")
print(f"Intersection (Two pointers): {intersection2.val if intersection2 else None}")
print(f"Intersection (Length diff): {intersection3.val if intersection3 else None}")
print(f"Intersection (Brute force): {intersection4.val if intersection4 else None}")
print(f"Intersection (Optimized): {intersection5.val if intersection5 else None}")
print(f"Intersection (Distance): {intersection6.val if intersection6 else None}")
