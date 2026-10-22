# Question 26: Find the first and last occurrence of a character.

text = input("Enter a string: ")
ch = input("Enter a character: ")

first = text.find(ch)
last = text.rfind(ch)

if first == -1:
    print("Character not found")
else:
    print("First occurrence at index:", first)
    print("Last occurrence at index:", last)


# ----- Output -----
# Enter a string: programming
# Enter a character: g
# First occurrence at index: 3
# Last occurrence at index: 10
