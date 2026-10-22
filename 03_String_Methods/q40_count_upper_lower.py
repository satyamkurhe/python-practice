# Question 40: Count uppercase and lowercase letters separately.

text = input("Enter a string: ")
upper = 0
lower = 0

for ch in text:
    if ch.isupper():
        upper = upper + 1
    elif ch.islower():
        lower = lower + 1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)


# ----- Output -----
# Enter a string: Hello World Python
# Uppercase letters: 3
# Lowercase letters: 13
