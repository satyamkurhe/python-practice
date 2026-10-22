# Question 36: Remove duplicate characters from a string.

text = input("Enter a string: ")
result = ""

for ch in text:
    if ch not in result:
        result = result + ch

print("After removing duplicates:", result)


# ----- Output -----
# Enter a string: programming
# After removing duplicates: progamin
