# Question 4: Count the number of vowels in a string.

text = input("Enter a string: ").lower()
count = 0

for vowel in "aeiou":
    count = count + text.count(vowel)

print("Number of vowels:", count)


# ----- Output -----
# Enter a string: Python Programming
# Number of vowels: 4
