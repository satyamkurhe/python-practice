# Question 10: Find the index of a given character in a string.

text = input("Enter a string: ")
ch = input("Enter a character to find: ")

index = text.find(ch)

if index != -1:
    print("Index of", ch, "is", index)
else:
    print("Character not found")


# ----- Output -----
# Enter a string: programming
# Enter a character to find: g
# Index of g is 3
