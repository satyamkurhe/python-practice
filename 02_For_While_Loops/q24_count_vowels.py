# Question 24: Count vowels in a string.

text = input("Enter a string: ")
count = 0

for ch in text.lower():
    if ch in "aeiou":
        count = count + 1

print("Number of vowels:", count)


# ----- Output -----
# Enter a string: Programming Language
# Number of vowels: 7
