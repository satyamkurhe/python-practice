# Question 22: Reverse a string using string methods.

text = input("Enter a string: ")

# reversed() gives characters in reverse order, join() combines them
reverse = "".join(reversed(text))

print("Reversed string:", reverse)


# ----- Output -----
# Enter a string: Python
# Reversed string: nohtyP
