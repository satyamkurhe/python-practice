# Question 21: Write a program to find the smallest of three numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a <= b and a <= c:
    print("Smallest number is", a)
elif b <= a and b <= c:
    print("Smallest number is", b)
else:
    print("Smallest number is", c)


# ----- Output -----
# Enter first number: 12
# Enter second number: 56
# Enter third number: 34
# Smallest number is 12
