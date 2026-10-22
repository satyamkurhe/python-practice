# Question 16: Write a program to find the greatest of three numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Greatest number is", a)
elif b >= a and b >= c:
    print("Greatest number is", b)
else:
    print("Greatest number is", c)


# ----- Output -----
# Enter first number: 12
# Enter second number: 56
# Enter third number: 34
# Greatest number is 56
