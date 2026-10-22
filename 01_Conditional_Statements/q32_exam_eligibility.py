# Question 32: Write a program to check whether a student is eligible for an exam (attendance + marks).

attendance = float(input("Enter attendance percentage: "))
marks = int(input("Enter internal marks: "))

if attendance >= 75:
    if marks >= 35:
        print("Eligible for the exam")
    else:
        print("Not eligible: internal marks are less than 35")
else:
    print("Not eligible: attendance is less than 75%")


# ----- Output -----
# Enter attendance percentage: 80
# Enter internal marks: 45
# Eligible for the exam
