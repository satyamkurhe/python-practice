# Question 5: Count the number of consonants in a string.

text = input("Enter a string: ").lower()
vowels = 0

for vowel in "aeiou":
    vowels = vowels + text.count(vowel)

letters = 0
for ch in text:
    if ch.isalpha():
        letters = letters + 1

print("Number of consonants:", letters - vowels)


# ----- Output -----
# Enter a string: Python Programming
# Number of consonants: 13
