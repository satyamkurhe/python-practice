# Question 31: Write a program to check whether a number is positive and even using nested if.

num = int(input("Enter a number: "))

if num > 0:
    if num % 2 == 0:
        print("The number is Positive and Even")
    else:
        print("The number is Positive but Odd")
else:
    print("The number is not Positive")


# ----- Output -----
# Enter a number: 24
# The number is Positive and Even
