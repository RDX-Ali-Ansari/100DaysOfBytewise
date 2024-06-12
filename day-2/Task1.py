def is_palindrome(word):
    if word == word[::-1]:
        return f"{word} is a palindrome."
    else:
        return f"{word} is not a palindrome."

# Example usage
print(is_palindrome("racecar"))
print(is_palindrome("Python"))
