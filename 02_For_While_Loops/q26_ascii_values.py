# Question 26: Print ASCII values of characters in a string.

text = input("Enter a string: ")

for ch in text:
    print(ch, "->", ord(ch))


# ----- Output -----
# Enter a string: Hello
# H -> 72
# e -> 101
# l -> 108
# l -> 108
# o -> 111
