# Question 34: Find the ASCII value of each character in a string.

text = input("Enter a string: ")

for ch in text:
    print(ch, "->", ord(ch))


# ----- Output -----
# Enter a string: Abc
# A -> 65
# b -> 98
# c -> 99
