# Question 37: Find the longest word in a sentence.

sentence = input("Enter a sentence: ")
words = sentence.split()

longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)


# ----- Output -----
# Enter a sentence: Python is a wonderful programming language
# Longest word: programming
