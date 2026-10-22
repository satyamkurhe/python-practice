# Question 32: Calculate power of a number without using pow().

base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))
result = 1

for i in range(exp):
    result = result * base

print(base, "raised to the power", exp, "is", result)


# ----- Output -----
# Enter base: 2
# Enter exponent: 10
# 2 raised to the power 10 is 1024
