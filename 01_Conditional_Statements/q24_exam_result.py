# Question 24: Write a program to check exam results (Distinction, First Class, Pass, Fail).

percentage = float(input("Enter percentage: "))

if percentage >= 75:
    print("Result: Distinction")
elif percentage >= 60:
    print("Result: First Class")
elif percentage >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")


# ----- Output -----
# Enter percentage: 68
# Result: First Class
