# Question 6: Write a program to compare two numbers and print the greater one.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(a, "is greater")
elif b > a:
    print(b, "is greater")
else:
    print("Both numbers are equal")


# ----- Output -----
# Enter first number: 45
# Enter second number: 78
# 78 is greater
