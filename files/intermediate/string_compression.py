def compress_string(text):
    if not text:
        return ""
    
    compressed = ""
    count = 1
    current_char = text[0]
    
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            compressed += current_char + str(count)
            current_char = text[i]
            count = 1
    
    compressed += current_char + str(count)
    return compressed

def decompress_string(compressed):
    if not compressed:
        return ""
    
    decompressed = ""
    i = 0
    
    while i < len(compressed):
        char = compressed[i]
        i += 1
        count_str = ""
        
        while i < len(compressed) and compressed[i].isdigit():
            count_str += compressed[i]
            i += 1
        
        count = int(count_str) if count_str else 1
        decompressed += char * count
    
    return decompressed

text = "aaabbbccc"
compressed = compress_string(text)
decompressed = decompress_string(compressed)

print(f"Original: {text}")
print(f"Compressed: {compressed}")
print(f"Decompressed: {decompressed}")
