# Question 25: Extract only alphabets from a string.

text = input("Enter a string: ")
letters = ""

for ch in text:
    if ch.isalpha():
        letters = letters + ch

print("Alphabets:", letters)


# ----- Output -----
# Enter a string: abc123def45gh6
# Alphabets: abcdefgh
