def is_valid_number_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_valid_number_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def is_valid_number_regex(s):
    import re
    pattern = r'^[+-]?(\d+\.?\d*|\.\d+)([eE][+-]?\d+)?$'
    return bool(re.match(pattern, s.strip()))

def is_valid_number_manual(s):
    s = s.strip()
    if not s:
        return False
    
    has_digit = False
    has_dot = False
    has_e = False
    has_sign = False
    
    for i, char in enumerate(s):
        if char.isdigit():
            has_digit = True
        elif char == '.':
            if has_dot or has_e:
                return False
            has_dot = True
        elif char in 'eE':
            if has_e or not has_digit:
                return False
            has_e = True
            has_digit = False
        elif char in '+-':
            if i != 0 and s[i-1] not in 'eE':
                return False
            has_sign = True
        else:
            return False
    
    return has_digit

def is_valid_number_with_validation(s):
    if not s or not isinstance(s, str):
        return False
    
    s = s.strip()
    if not s:
        return False
    
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_valid_number_with_constraints(s, constraints):
    if not constraints(s):
        return False
    
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_valid_number_with_optimization(s):
    s = s.strip()
    if not s:
        return False
    
    has_digit = False
    has_dot = False
    has_e = False
    
    for i, char in enumerate(s):
        if char.isdigit():
            has_digit = True
        elif char == '.':
            if has_dot or has_e:
                return False
            has_dot = True
        elif char in 'eE':
            if has_e or not has_digit:
                return False
            has_e = True
            has_digit = False
        elif char in '+-':
            if i != 0 and s[i-1] not in 'eE':
                return False
        else:
            return False
    
    return has_digit

def is_valid_number_with_advanced_optimization(s):
    s = s.strip()
    if not s:
        return False
    
    has_digit = False
    has_dot = False
    has_e = False
    
    for i, char in enumerate(s):
        if char.isdigit():
            has_digit = True
        elif char == '.':
            if has_dot or has_e:
                return False
            has_dot = True
        elif char in 'eE':
            if has_e or not has_digit:
                return False
            has_e = True
            has_digit = False
        elif char in '+-':
            if i != 0 and s[i-1] not in 'eE':
                return False
        else:
            return False
    
    return has_digit

def is_valid_number_with_count(s):
    s = s.strip()
    if not s:
        return False, 0
    
    has_digit = False
    has_dot = False
    has_e = False
    digit_count = 0
    
    for i, char in enumerate(s):
        if char.isdigit():
            has_digit = True
            digit_count += 1
        elif char == '.':
            if has_dot or has_e:
                return False, 0
            has_dot = True
        elif char in 'eE':
            if has_e or not has_digit:
                return False, 0
            has_e = True
            has_digit = False
        elif char in '+-':
            if i != 0 and s[i-1] not in 'eE':
                return False, 0
        else:
            return False, 0
    
    return has_digit, digit_count

def is_valid_number_with_analysis(s):
    s = s.strip()
    if not s:
        return False, {}
    
    has_digit = False
    has_dot = False
    has_e = False
    has_sign = False
    digit_count = 0
    dot_count = 0
    e_count = 0
    sign_count = 0
    
    for i, char in enumerate(s):
        if char.isdigit():
            has_digit = True
            digit_count += 1
        elif char == '.':
            if has_dot or has_e:
                return False, {}
            has_dot = True
            dot_count += 1
        elif char in 'eE':
            if has_e or not has_digit:
                return False, {}
            has_e = True
            has_digit = False
            e_count += 1
        elif char in '+-':
            if i != 0 and s[i-1] not in 'eE':
                return False, {}
            has_sign = True
            sign_count += 1
        else:
            return False, {}
    
    analysis = {
        'has_digit': has_digit,
        'has_dot': has_dot,
        'has_e': has_e,
        'has_sign': has_sign,
        'digit_count': digit_count,
        'dot_count': dot_count,
        'e_count': e_count,
        'sign_count': sign_count
    }
    
    return has_digit, analysis

def is_valid_number_with_validation_enhanced(s):
    if not s or not isinstance(s, str):
        return False
    
    s = s.strip()
    if not s:
        return False
    
    if len(s) > 1000:
        return False
    
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_valid_number_with_optimization_enhanced(s):
    s = s.strip()
    if not s:
        return False
    
    if len(s) > 1000:
        return False
    
    has_digit = False
    has_dot = False
    has_e = False
    
    for i, char in enumerate(s):
        if char.isdigit():
            has_digit = True
        elif char == '.':
            if has_dot or has_e:
                return False
            has_dot = True
        elif char in 'eE':
            if has_e or not has_digit:
                return False
            has_e = True
            has_digit = False
        elif char in '+-':
            if i != 0 and s[i-1] not in 'eE':
                return False
        else:
            return False
    
    return has_digit

def is_valid_number_with_advanced_optimization_enhanced(s):
    s = s.strip()
    if not s:
        return False
    
    if len(s) > 1000:
        return False
    
    has_digit = False
    has_dot = False
    has_e = False
    
    for i, char in enumerate(s):
        if char.isdigit():
            has_digit = True
        elif char == '.':
            if has_dot or has_e:
                return False
            has_dot = True
        elif char in 'eE':
            if has_e or not has_digit:
                return False
            has_e = True
            has_digit = False
        elif char in '+-':
            if i != 0 and s[i-1] not in 'eE':
                return False
        else:
            return False
    
    return has_digit

test_strings = ["123", "12.34", "1e5", "1.2e-3", "abc", "12.34.56", "1e", "e5"]

for s in test_strings:
    valid1 = is_valid_number_float(s)
    valid2 = is_valid_number_integer(s)
    valid3 = is_valid_number_regex(s)
    valid4 = is_valid_number_manual(s)
    valid5 = is_valid_number_with_validation(s)
    valid6 = is_valid_number_with_optimization(s)
    valid7 = is_valid_number_with_advanced_optimization(s)
    valid8, count = is_valid_number_with_count(s)
    valid9, analysis = is_valid_number_with_analysis(s)
    valid10 = is_valid_number_with_validation_enhanced(s)
    valid11 = is_valid_number_with_optimization_enhanced(s)
    valid12 = is_valid_number_with_advanced_optimization_enhanced(s)
    
    print(f"String: '{s}'")
    print(f"Valid (float): {valid1}")
    print(f"Valid (integer): {valid2}")
    print(f"Valid (regex): {valid3}")
    print(f"Valid (manual): {valid4}")
    print(f"Valid (with validation): {valid5}")
    print(f"Valid (with optimization): {valid6}")
    print(f"Valid (advanced optimization): {valid7}")
    print(f"Valid (with count): {valid8}, Count: {count}")
    print(f"Valid (with analysis): {valid9}, Analysis: {analysis}")
    print(f"Valid (validation enhanced): {valid10}")
    print(f"Valid (optimization enhanced): {valid11}")
    print(f"Valid (advanced optimization enhanced): {valid12}")
    print()
