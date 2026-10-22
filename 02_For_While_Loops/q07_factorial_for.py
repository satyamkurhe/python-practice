# Question 7: Calculate factorial of a number using for loop.

n = int(input("Enter a number: "))
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial of", n, "is", fact)


# ----- Output -----
# Enter a number: 6
# Factorial of 6 is 720
