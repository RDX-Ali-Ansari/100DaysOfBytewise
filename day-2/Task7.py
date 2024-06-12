import re

def is_palindrome_sentence(sentence):
    cleaned_sentence = re.sub(r'[^A-Za-z]', '', sentence).lower()
    if cleaned_sentence == cleaned_sentence[::-1]:
        return f"{sentence} is a palindrome."
    else:
        return f"{sentence} is not a palindrome."

# Example usage
print(is_palindrome_sentence("A man, a plan, a canal: Panama"))
print(is_palindrome_sentence("Hello, world!"))
