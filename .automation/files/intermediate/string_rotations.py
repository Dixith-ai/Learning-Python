def are_rotations(str1, str2):
    if len(str1) != len(str2):
        return False
    
    concatenated = str1 + str1
    return str2 in concatenated

def are_rotations_manual(str1, str2):
    if len(str1) != len(str2):
        return False
    
    n = len(str1)
    for i in range(n):
        rotated = str1[i:] + str1[:i]
        if rotated == str2:
            return True
    
    return False

def get_all_rotations(text):
    rotations = []
    n = len(text)
    
    for i in range(n):
        rotation = text[i:] + text[:i]
        rotations.append(rotation)
    
    return rotations

str1 = "abcd"
str2 = "cdab"
str3 = "bcda"

are_rot1 = are_rotations(str1, str2)
are_rot2 = are_rotations_manual(str1, str2)
are_rot3 = are_rotations(str1, str3)
rotations = get_all_rotations(str1)

print(f"String 1: {str1}")
print(f"String 2: {str2}")
print(f"Are rotations: {are_rot1}")
print(f"Are rotations (manual): {are_rot2}")
print(f"String 3: {str3}")
print(f"Are rotations: {are_rot3}")
print(f"All rotations: {rotations}")
