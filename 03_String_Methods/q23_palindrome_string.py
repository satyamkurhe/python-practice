# Question 23: Check whether a string is a palindrome.

text = input("Enter a string: ").lower()
reverse = "".join(reversed(text))

if text == reverse:
    print("The string is a Palindrome")
else:
    print("The string is not a Palindrome")


# ----- Output -----
# Enter a string: Madam
# The string is a Palindrome
