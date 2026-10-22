# Question 31: Remove punctuation marks from a string.

import string

text = input("Enter a string: ")

# translate() with a table removes every punctuation character
clean = text.translate(str.maketrans("", "", string.punctuation))

print("Without punctuation:", clean)


# ----- Output -----
# Enter a string: Hello, World! How's it going?
# Without punctuation: Hello World Hows it going
