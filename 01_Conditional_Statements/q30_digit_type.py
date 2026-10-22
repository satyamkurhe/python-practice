# Question 30: Write a program to check the type of number (single, double, or three digit).

num = abs(int(input("Enter a number: ")))

if num < 10:
    print("Single digit number")
elif num < 100:
    print("Double digit number")
elif num < 1000:
    print("Three digit number")
else:
    print("Number has more than three digits")


# ----- Output -----
# Enter a number: 456
# Three digit number
