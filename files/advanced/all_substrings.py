def get_all_substrings(text):
    substrings = []
    n = len(text)
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            substrings.append(text[i:j])
    
    return substrings

def get_all_substrings_unique(text):
    substrings = set()
    n = len(text)
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            substrings.add(text[i:j])
    
    return list(substrings)

def get_all_substrings_length_k(text, k):
    substrings = []
    n = len(text)
    
    for i in range(n - k + 1):
        substrings.append(text[i:i + k])
    
    return substrings

text = "abc"
all_subs = get_all_substrings(text)
unique_subs = get_all_substrings_unique(text)
length_2_subs = get_all_substrings_length_k(text, 2)

print(f"Text: {text}")
print(f"All substrings: {all_subs}")
print(f"Unique substrings: {unique_subs}")
print(f"Length 2 substrings: {length_2_subs}")
