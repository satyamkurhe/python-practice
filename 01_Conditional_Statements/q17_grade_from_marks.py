# Question 17: Write a program to check grade based on marks (A, B, C, Fail).

marks = int(input("Enter marks (0-100): "))

if marks >= 75:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 40:
    print("Grade: C")
else:
    print("Grade: Fail")


# ----- Output -----
# Enter marks (0-100): 72
# Grade: B
