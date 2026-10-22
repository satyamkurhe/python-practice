# Question 46: Print first n multiples of a number.

num = int(input("Enter a number: "))
n = int(input("How many multiples do you want? "))

for i in range(1, n + 1):
    print(num * i, end=" ")
print()


# ----- Output -----
# Enter a number: 6
# How many multiples do you want? 5
# 6 12 18 24 30
