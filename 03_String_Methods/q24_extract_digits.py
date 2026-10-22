# Question 24: Extract only digits from a string.

text = input("Enter a string: ")
digits = ""

for ch in text:
    if ch.isdigit():
        digits = digits + ch

print("Digits:", digits)


# ----- Output -----
# Enter a string: abc123def45gh6
# Digits: 123456
