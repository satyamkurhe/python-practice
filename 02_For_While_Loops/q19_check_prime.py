# Question 19: Check whether a number is prime.

num = int(input("Enter a number: "))
is_prime = True

if num < 2:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(num, "is a Prime number")
else:
    print(num, "is not a Prime number")


# ----- Output -----
# Enter a number: 29
# 29 is a Prime number
