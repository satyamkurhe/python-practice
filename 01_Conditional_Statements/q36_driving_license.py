# Question 36: Write a program to check whether a person is eligible for a driving license.

age = int(input("Enter age: "))
test = input("Have you passed the driving test? (yes/no): ").lower()

if age >= 18:
    if test == "yes":
        print("You are eligible for a driving license")
    else:
        print("You must pass the driving test first")
else:
    print("You are not eligible: minimum age is 18")


# ----- Output -----
# Enter age: 20
# Have you passed the driving test? (yes/no): yes
# You are eligible for a driving license
