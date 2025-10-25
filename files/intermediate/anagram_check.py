def are_anagrams(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

def are_anagrams_count(str1, str2):
    if len(str1) != len(str2):
        return False
    
    count = {}
    
    for char in str1.lower():
        count[char] = count.get(char, 0) + 1
    
    for char in str2.lower():
        if char not in count:
            return False
        count[char] -= 1
        if count[char] == 0:
            del count[char]
    
    return len(count) == 0

def are_anagrams_counter(str1, str2):
    from collections import Counter
    return Counter(str1.lower()) == Counter(str2.lower())

str1 = "listen"
str2 = "silent"

anagram1 = are_anagrams(str1, str2)
anagram2 = are_anagrams_count(str1, str2)
anagram3 = are_anagrams_counter(str1, str2)

print(f"String 1: {str1}")
print(f"String 2: {str2}")
print(f"Are anagrams (sorted): {anagram1}")
print(f"Are anagrams (count): {anagram2}")
print(f"Are anagrams (Counter): {anagram3}")
