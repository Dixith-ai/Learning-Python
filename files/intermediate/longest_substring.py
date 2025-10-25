def longest_substring_no_repeat(text):
    if not text:
        return 0
    
    char_index = {}
    start = 0
    max_length = 0
    
    for end in range(len(text)):
        if text[end] in char_index and char_index[text[end]] >= start:
            start = char_index[text[end]] + 1
        
        char_index[text[end]] = end
        max_length = max(max_length, end - start + 1)
    
    return max_length

def longest_substring_no_repeat_sliding(text):
    if not text:
        return 0
    
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(text)):
        while text[right] in char_set:
            char_set.remove(text[left])
            left += 1
        
        char_set.add(text[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length

text = "abcabcbb"
length1 = longest_substring_no_repeat(text)
length2 = longest_substring_no_repeat_sliding(text)

print(f"Text: {text}")
print(f"Longest substring length: {length1}")
print(f"Longest substring length (sliding): {length2}")
