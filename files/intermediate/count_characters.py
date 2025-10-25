def count_characters(text):
    char_count = {}
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

def count_characters_counter(text):
    from collections import Counter
    return dict(Counter(text))

def count_characters_case_insensitive(text):
    char_count = {}
    for char in text.lower():
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

def count_characters_ignore_spaces(text):
    char_count = {}
    for char in text:
        if char != ' ':
            char_count[char] = char_count.get(char, 0) + 1
    return char_count

text = "Hello World"

count1 = count_characters(text)
count2 = count_characters_counter(text)
count3 = count_characters_case_insensitive(text)
count4 = count_characters_ignore_spaces(text)

print(f"Text: {text}")
print(f"Character count: {count1}")
print(f"Character count (Counter): {count2}")
print(f"Character count (case insensitive): {count3}")
print(f"Character count (ignore spaces): {count4}")
