# Question 34: Check whether a string is palindrome.

text = input("Enter a string: ")
reverse = ""

for ch in text:
    reverse = ch + reverse

if text.lower() == reverse.lower():
    print(text, "is a Palindrome string")
else:
    print(text, "is not a Palindrome string")


# ----- Output -----
# Enter a string: madam
# madam is a Palindrome string
