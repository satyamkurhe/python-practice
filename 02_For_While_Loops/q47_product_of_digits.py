# Question 47: Find product of digits of a number.

num = int(input("Enter a number: "))
product = 1

while num > 0:
    product = product * (num % 10)
    num = num // 10

print("Product of digits:", product)


# ----- Output -----
# Enter a number: 2345
# Product of digits: 120
