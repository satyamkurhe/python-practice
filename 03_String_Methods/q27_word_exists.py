# Question 27: Check whether a word exists in a sentence.

sentence = input("Enter a sentence: ")
word = input("Enter a word to search: ")

if word in sentence.split():
    print("The word", word, "exists in the sentence")
else:
    print("The word", word, "does not exist in the sentence")


# ----- Output -----
# Enter a sentence: Python is easy to learn
# Enter a word to search: easy
# The word easy exists in the sentence
