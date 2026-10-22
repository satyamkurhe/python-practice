# Question 33: Write a program to check whether a person can apply for a loan.

age = int(input("Enter age: "))
salary = int(input("Enter monthly salary: "))

if age >= 21 and age <= 60:
    if salary >= 25000:
        print("You can apply for a loan")
    else:
        print("You cannot apply: salary is less than Rs. 25000")
else:
    print("You cannot apply: age must be between 21 and 60")


# ----- Output -----
# Enter age: 30
# Enter monthly salary: 40000
# You can apply for a loan
