def are_anagrams(str1, str2):
    if sorted(str1) == sorted(str2):
        return f"{str1} and {str2} are anagrams."
    else:
        return f"{str1} and {str2} are not anagrams."

# Example usage
print(are_anagrams("listen", "silent"))
print(are_anagrams("python", "java"))
