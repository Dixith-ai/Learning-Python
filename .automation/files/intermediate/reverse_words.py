def reverse_words_sentence(sentence):
    words = sentence.split()
    return ' '.join(words[::-1])

def reverse_words_sentence_loop(sentence):
    words = sentence.split()
    reversed_words = []
    
    for i in range(len(words) - 1, -1, -1):
        reversed_words.append(words[i])
    
    return ' '.join(reversed_words)

def reverse_words_keep_order(sentence):
    words = sentence.split()
    reversed_sentence = []
    
    for word in words:
        reversed_sentence.append(word[::-1])
    
    return ' '.join(reversed_sentence)

sentence = "Hello World Python Programming"

reversed1 = reverse_words_sentence(sentence)
reversed2 = reverse_words_sentence_loop(sentence)
reversed3 = reverse_words_keep_order(sentence)

print(f"Original: {sentence}")
print(f"Reversed words: {reversed1}")
print(f"Reversed words (loop): {reversed2}")
print(f"Reversed characters in words: {reversed3}")
