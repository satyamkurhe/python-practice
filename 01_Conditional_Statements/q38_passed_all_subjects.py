# Question 38: Write a program to check whether a student passed all subjects.

maths = int(input("Enter Maths marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))

if maths >= 40 and science >= 40 and english >= 40:
    print("Student has passed all subjects")
else:
    print("Student has failed in one or more subjects")


# ----- Output -----
# Enter Maths marks: 56
# Enter Science marks: 72
# Enter English marks: 38
# Student has failed in one or more subjects
