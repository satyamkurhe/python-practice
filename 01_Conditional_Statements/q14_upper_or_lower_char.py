# Question 14: Write a program to check whether a given character is uppercase or lowercase.

ch = input("Enter a character: ")

if ch.isupper():
    print("The character is Uppercase")
elif ch.islower():
    print("The character is Lowercase")
else:
    print("The character is not an alphabet")


# ----- Output -----
# Enter a character: G
# The character is Uppercase
