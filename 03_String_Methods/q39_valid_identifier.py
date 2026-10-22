# Question 39: Check whether a string is a valid identifier.

text = input("Enter a string: ")

if text.isidentifier():
    print("The string is a valid identifier")
else:
    print("The string is not a valid identifier")


# ----- Output -----
# Enter a string: my_variable1
# The string is a valid identifier
