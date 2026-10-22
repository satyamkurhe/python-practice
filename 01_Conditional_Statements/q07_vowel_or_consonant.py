# Question 7: Write a program to check whether a character is a vowel or consonant.

ch = input("Enter a character: ").lower()

if ch in "aeiou":
    print("The character is a Vowel")
else:
    print("The character is a Consonant")


# ----- Output -----
# Enter a character: e
# The character is a Vowel
