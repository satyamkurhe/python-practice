# Question 38: Find the shortest word in a sentence.

sentence = input("Enter a sentence: ")
words = sentence.split()

shortest = words[0]
for word in words:
    if len(word) < len(shortest):
        shortest = word

print("Shortest word:", shortest)


# ----- Output -----
# Enter a sentence: Python is a wonderful programming language
# Shortest word: a
