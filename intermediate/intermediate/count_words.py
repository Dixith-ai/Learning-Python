def count_words(text):
    words = text.split()
    return len(words)

def count_words_manual(text):
    count = 0
    in_word = False
    
    for char in text:
        if char.isalnum() and not in_word:
            count += 1
            in_word = True
        elif not char.isalnum():
            in_word = False
    
    return count

text = "Hello World Python Programming"
word_count = count_words(text)
word_count_manual = count_words_manual(text)
print(f"Text: {text}")
print(f"Word count (split): {word_count}")
print(f"Word count (manual): {word_count_manual}")
