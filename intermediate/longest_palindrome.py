def longest_palindrome_substring(text):
    if not text:
        return ""
    
    start = 0
    max_length = 1
    
    def expand_around_center(left, right):
        while left >= 0 and right < len(text) and text[left] == text[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    for i in range(len(text)):
        len1 = expand_around_center(i, i)
        len2 = expand_around_center(i, i + 1)
        
        current_max = max(len1, len2)
        
        if current_max > max_length:
            max_length = current_max
            start = i - (current_max - 1) // 2
    
    return text[start:start + max_length]

def longest_palindrome_brute_force(text):
    if not text:
        return ""
    
    longest = ""
    
    for i in range(len(text)):
        for j in range(i, len(text)):
            substring = text[i:j+1]
            if substring == substring[::-1] and len(substring) > len(longest):
                longest = substring
    
    return longest

text = "babad"
longest1 = longest_palindrome_substring(text)
longest2 = longest_palindrome_brute_force(text)

print(f"Text: {text}")
print(f"Longest palindrome: {longest1}")
print(f"Longest palindrome (brute force): {longest2}")
