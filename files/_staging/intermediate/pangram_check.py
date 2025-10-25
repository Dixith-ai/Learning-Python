def is_pangram(text):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    text_lower = text.lower()
    text_letters = set(char for char in text_lower if char.isalpha())
    return alphabet.issubset(text_letters)

def is_pangram_ascii(text):
    text_lower = text.lower()
    used_letters = set()
    
    for char in text_lower:
        if char.isalpha():
            used_letters.add(char)
    
    return len(used_letters) == 26

def is_pangram_bitwise(text):
    text_lower = text.lower()
    bit_mask = 0
    
    for char in text_lower:
        if char.isalpha():
            bit_mask |= (1 << (ord(char) - ord('a')))
    
    return bit_mask == (1 << 26) - 1

text1 = "The quick brown fox jumps over the lazy dog"
text2 = "Hello world"

pangram1 = is_pangram(text1)
pangram2 = is_pangram(text2)
pangram_ascii1 = is_pangram_ascii(text1)
pangram_bitwise1 = is_pangram_bitwise(text1)

print(f"Text 1: {text1}")
print(f"Is pangram: {pangram1}")
print(f"Is pangram (ASCII): {pangram_ascii1}")
print(f"Is pangram (bitwise): {pangram_bitwise1}")

print(f"Text 2: {text2}")
print(f"Is pangram: {is_pangram(text2)}")
