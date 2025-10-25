def evaluate_postfix_expression(expression):
    stack = []
    operators = {'+', '-', '*', '/', '^'}
    
    for token in expression.split():
        if token in operators:
            if len(stack) < 2:
                raise ValueError("Invalid postfix expression")
            
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                if b == 0:
                    raise ValueError("Division by zero")
                result = a / b
            elif token == '^':
                result = a ** b
            
            stack.append(result)
        else:
            try:
                stack.append(float(token))
            except ValueError:
                raise ValueError(f"Invalid token: {token}")
    
    if len(stack) != 1:
        raise ValueError("Invalid postfix expression")
    
    return stack[0]

def evaluate_postfix_list(expression):
    stack = []
    operators = {'+', '-', '*', '/', '^'}
    
    for token in expression:
        if token in operators:
            if len(stack) < 2:
                raise ValueError("Invalid postfix expression")
            
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                if b == 0:
                    raise ValueError("Division by zero")
                result = a / b
            elif token == '^':
                result = a ** b
            
            stack.append(result)
        else:
            try:
                stack.append(float(token))
            except ValueError:
                raise ValueError(f"Invalid token: {token}")
    
    if len(stack) != 1:
        raise ValueError("Invalid postfix expression")
    
    return stack[0]

def evaluate_postfix_with_validation(expression):
    stack = []
    operators = {'+', '-', '*', '/', '^'}
    
    for i, token in enumerate(expression.split()):
        if token in operators:
            if len(stack) < 2:
                raise ValueError(f"Invalid postfix expression at position {i}: insufficient operands")
            
            b = stack.pop()
            a = stack.pop()
            
            try:
                if token == '+':
                    result = a + b
                elif token == '-':
                    result = a - b
                elif token == '*':
                    result = a * b
                elif token == '/':
                    if b == 0:
                        raise ValueError(f"Division by zero at position {i}")
                    result = a / b
                elif token == '^':
                    result = a ** b
                
                stack.append(result)
            except Exception as e:
                raise ValueError(f"Error at position {i}: {e}")
        else:
            try:
                stack.append(float(token))
            except ValueError:
                raise ValueError(f"Invalid token at position {i}: {token}")
    
    if len(stack) != 1:
        raise ValueError("Invalid postfix expression: too many operands")
    
    return stack[0]

def evaluate_postfix_recursive(expression):
    def helper(tokens, index):
        if index >= len(tokens):
            return None, index
        
        token = tokens[index]
        
        if token in {'+', '-', '*', '/', '^'}:
            left, index = helper(tokens, index + 1)
            right, index = helper(tokens, index)
            
            if left is None or right is None:
                return None, index
            
            if token == '+':
                return left + right, index
            elif token == '-':
                return left - right, index
            elif token == '*':
                return left * right, index
            elif token == '/':
                if right == 0:
                    raise ValueError("Division by zero")
                return left / right, index
            elif token == '^':
                return left ** right, index
        else:
            try:
                return float(token), index + 1
            except ValueError:
                raise ValueError(f"Invalid token: {token}")
    
    tokens = expression.split()
    result, _ = helper(tokens, 0)
    return result

expressions = [
    "3 4 + 2 * 1 +",
    "5 1 2 + 4 * + 3 -",
    "2 3 + 4 *",
    "1 2 + 3 4 + *"
]

for expr in expressions:
    try:
        result1 = evaluate_postfix_expression(expr)
        result2 = evaluate_postfix_list(expr.split())
        result3 = evaluate_postfix_with_validation(expr)
        print(f"'{expr}' = {result1} {result2} {result3}")
    except Exception as e:
        print(f"Error evaluating '{expr}': {e}")
