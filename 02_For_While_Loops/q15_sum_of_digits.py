# Question 15: Find sum of digits of a number.

num = int(input("Enter a number: "))
total = 0

while num > 0:
    total = total + num % 10
    num = num // 10

print("Sum of digits:", total)


# ----- Output -----
# Enter a number: 4567
# Sum of digits: 22
