# Question 21: Find the length of a string without using len().

text = input("Enter a string: ")
count = 0

for ch in text:
    count = count + 1

print("Length of the string:", count)


# ----- Output -----
# Enter a string: Hello Python
# Length of the string: 12
