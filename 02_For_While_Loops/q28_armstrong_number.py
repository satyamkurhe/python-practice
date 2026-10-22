# Question 28: Check whether a number is Armstrong.

num = int(input("Enter a number: "))
original = num
digits = len(str(num))
total = 0

while num > 0:
    digit = num % 10
    total = total + digit ** digits
    num = num // 10

if total == original:
    print(original, "is an Armstrong number")
else:
    print(original, "is not an Armstrong number")


# ----- Output -----
# Enter a number: 153
# 153 is an Armstrong number
