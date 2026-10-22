# Question 7: Check whether a string ends with a given substring.

text = input("Enter a string: ")
sub = input("Enter the substring: ")

if text.endswith(sub):
    print("The string ends with", sub)
else:
    print("The string does not end with", sub)


# ----- Output -----
# Enter a string: Python is fun
# Enter the substring: fun
# The string ends with fun
