def get_permutations(text):
    if len(text) == 1:
        return [text]
    
    permutations = []
    for i in range(len(text)):
        char = text[i]
        remaining = text[:i] + text[i+1:]
        
        for perm in get_permutations(remaining):
            permutations.append(char + perm)
    
    return permutations

def get_permutations_iterative(text):
    from itertools import permutations
    return [''.join(p) for p in permutations(text)]

def get_permutations_unique(text):
    permutations = get_permutations(text)
    return list(set(permutations))

text = "abc"
perms = get_permutations(text)
perms_iter = get_permutations_iterative(text)
perms_unique = get_permutations_unique("aab")

print(f"Text: {text}")
print(f"Permutations: {perms}")
print(f"Permutations (iterative): {perms_iter}")
print(f"Unique permutations of 'aab': {perms_unique}")
