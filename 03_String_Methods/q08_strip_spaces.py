# Question 8: Remove leading and trailing spaces from a string.

text = input("Enter a string: ")

print("Before:", "[" + text + "]")
print("After :", "[" + text.strip() + "]")


# ----- Output -----
# Enter a string:    Hello Python
# Before: [   Hello Python   ]
# After : [Hello Python]
