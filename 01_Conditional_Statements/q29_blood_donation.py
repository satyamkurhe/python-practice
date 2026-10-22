# Question 29: Write a program to check blood donation eligibility based on age and weight.

age = int(input("Enter age: "))
weight = float(input("Enter weight in kg: "))

if age >= 18 and age <= 65 and weight >= 50:
    print("You are eligible to donate blood")
else:
    print("You are not eligible to donate blood")


# ----- Output -----
# Enter age: 25
# Enter weight in kg: 62
# You are eligible to donate blood
