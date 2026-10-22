# Question 5: Write a program to check whether a given year is a leap year or not.

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap year")
else:
    print(year, "is not a Leap year")


# ----- Output -----
# Enter a year: 2024
# 2024 is a Leap year
