def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

# Example usage
print(reverse_words("The quick brown fox jumps over the lazy dog."))
