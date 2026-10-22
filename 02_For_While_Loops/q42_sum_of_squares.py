# Question 42: Calculate sum of squares of first n numbers.

n = int(input("Enter n: "))
total = 0

for i in range(1, n + 1):
    total = total + i * i

print("Sum of squares of first", n, "numbers =", total)


# ----- Output -----
# Enter n: 5
# Sum of squares of first 5 numbers = 55
