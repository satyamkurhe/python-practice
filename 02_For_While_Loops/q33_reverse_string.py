# Question 33: Print reverse of a string.

text = input("Enter a string: ")
reverse = ""

for ch in text:
    reverse = ch + reverse

print("Reversed string:", reverse)


# ----- Output -----
# Enter a string: Python
# Reversed string: nohtyP
