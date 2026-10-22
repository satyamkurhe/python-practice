# Question 13: Join a list of words into a single string.

data = input("Enter words separated by comma: ")
words = data.split(",")

print("List:", words)
print("Joined string:", " ".join(words))


# ----- Output -----
# Enter words separated by comma: Python,is,very,easy
# List: ['Python', 'is', 'very', 'easy']
# Joined string: Python is very easy
