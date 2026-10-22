# Question 43: Calculate sum of cubes of first n numbers.

n = int(input("Enter n: "))
total = 0

for i in range(1, n + 1):
    total = total + i ** 3

print("Sum of cubes of first", n, "numbers =", total)


# ----- Output -----
# Enter n: 5
# Sum of cubes of first 5 numbers = 225
