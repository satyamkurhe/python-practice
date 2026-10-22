# Question 39: Count total words in a string.

text = input("Enter a sentence: ")
count = 0

for word in text.split():
    count = count + 1

print("Total words:", count)


# ----- Output -----
# Enter a sentence: Python is easy to learn
# Total words: 5
