def is_palindrome_string(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

def is_palindrome_number(number):
    original_number = number
    reverse = 0
    
    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number //= 10
    
    return original_number == reverse

text = "racecar"
number = 121

if is_palindrome_string(text):
    print(f"'{text}' is a palindrome")
else:
    print(f"'{text}' is not a palindrome")

if is_palindrome_number(number):
    print(f"{number} is a palindrome number")
else:
    print(f"{number} is not a palindrome number")
