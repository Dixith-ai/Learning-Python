class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_sorted_lists_iterative(l1, l2):
    dummy = ListNode(0)
    current = dummy
    
    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    current.next = l1 or l2
    return dummy.next

def merge_sorted_lists_recursive(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    
    if l1.val <= l2.val:
        l1.next = merge_sorted_lists_recursive(l1.next, l2)
        return l1
    else:
        l2.next = merge_sorted_lists_recursive(l1, l2.next)
        return l2

def merge_sorted_lists_inplace(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    
    if l1.val > l2.val:
        l1, l2 = l2, l1
    
    head = l1
    
    while l1.next and l2:
        if l1.next.val <= l2.val:
            l1 = l1.next
        else:
            temp = l1.next
            l1.next = l2
            l2 = l2.next
            l1.next.next = temp
            l1 = l1.next
    
    if l2:
        l1.next = l2
    
    return head

def merge_sorted_lists_optimized(l1, l2):
    dummy = ListNode(0)
    tail = dummy
    
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    
    tail.next = l1 or l2
    return dummy.next

def merge_sorted_lists_with_duplicates(l1, l2):
    dummy = ListNode(0)
    current = dummy
    
    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    current.next = l1 or l2
    return dummy.next

def merge_sorted_lists_descending(l1, l2):
    dummy = ListNode(0)
    current = dummy
    
    while l1 and l2:
        if l1.val >= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    current.next = l1 or l2
    return dummy.next

def merge_k_sorted_lists(lists):
    if not lists:
        return None
    
    while len(lists) > 1:
        merged = []
        for i in range(0, len(lists), 2):
            if i + 1 < len(lists):
                merged.append(merge_sorted_lists_iterative(lists[i], lists[i + 1]))
            else:
                merged.append(lists[i])
        lists = merged
    
    return lists[0]

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

list1 = [1, 2, 4]
list2 = [1, 3, 4]
l1 = create_linked_list(list1)
l2 = create_linked_list(list2)

merged1 = merge_sorted_lists_iterative(l1, l2)
merged2 = merge_sorted_lists_recursive(create_linked_list(list1), create_linked_list(list2))
merged3 = merge_sorted_lists_inplace(create_linked_list(list1), create_linked_list(list2))
merged4 = merge_sorted_lists_optimized(create_linked_list(list1), create_linked_list(list2))

print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Merged (iterative): {print_linked_list(merged1)}")
print(f"Merged (recursive): {print_linked_list(merged2)}")
print(f"Merged (in-place): {print_linked_list(merged3)}")
print(f"Merged (optimized): {print_linked_list(merged4)}")

lists = [create_linked_list([1, 4, 5]), create_linked_list([1, 3, 4]), create_linked_list([2, 6])]
merged_k = merge_k_sorted_lists(lists)
print(f"Merged K lists: {print_linked_list(merged_k)}")
