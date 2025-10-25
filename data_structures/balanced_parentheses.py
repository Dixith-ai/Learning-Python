def is_balanced_parentheses_stack(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            stack.append(char)
    
    return not stack

def is_balanced_parentheses_counter(s):
    count = 0
    
    for char in s:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
            if count < 0:
                return False
    
    return count == 0

def is_balanced_parentheses_recursive(s):
    def helper(s, index, count):
        if index == len(s):
            return count == 0
        
        if s[index] == '(':
            return helper(s, index + 1, count + 1)
        elif s[index] == ')':
            if count == 0:
                return False
            return helper(s, index + 1, count - 1)
        else:
            return helper(s, index + 1, count)
    
    return helper(s, 0, 0)

def is_balanced_parentheses_iterative(s):
    count = 0
    
    for char in s:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
            if count < 0:
                return False
    
    return count == 0

def is_balanced_parentheses_all_types(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            stack.append(char)
    
    return not stack

def is_balanced_parentheses_with_positions(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for i, char in enumerate(s):
        if char in mapping:
            if not stack:
                return False, i
            if stack.pop()[0] != mapping[char]:
                return False, i
        else:
            stack.append((char, i))
    
    if stack:
        return False, stack[0][1]
    
    return True, -1

test_cases = [
    "()",
    "()[]{}",
    "(]",
    "([)]",
    "{[]}",
    "((()))",
    "(()())",
    "((())"
]

for test in test_cases:
    balanced1 = is_balanced_parentheses_stack(test)
    balanced2 = is_balanced_parentheses_counter(test)
    balanced3 = is_balanced_parentheses_recursive(test)
    balanced4 = is_balanced_parentheses_all_types(test)
    balanced5, pos = is_balanced_parentheses_with_positions(test)
    
    print(f"'{test}': {balanced1} {balanced2} {balanced3} {balanced4} {balanced5}")
