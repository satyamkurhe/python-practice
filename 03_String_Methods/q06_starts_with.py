# Question 6: Check whether a string starts with a given substring.

text = input("Enter a string: ")
sub = input("Enter the substring: ")

if text.startswith(sub):
    print("The string starts with", sub)
else:
    print("The string does not start with", sub)


# ----- Output -----
# Enter a string: Python is fun
# Enter the substring: Py
# The string starts with Py
