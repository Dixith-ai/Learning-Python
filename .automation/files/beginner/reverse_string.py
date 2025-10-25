def reverse_string(text):
    return text[::-1]

def reverse_string_loop(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text

text = "Hello World"
reversed_text = reverse_string(text)
reversed_text_loop = reverse_string_loop(text)
print(f"Original: {text}")
print(f"Reversed (slicing): {reversed_text}")
print(f"Reversed (loop): {reversed_text_loop}")
