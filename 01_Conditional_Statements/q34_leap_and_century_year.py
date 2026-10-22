# Question 34: Write a program to check whether a year is a leap year and century year.

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap year")
    if year % 100 == 0:
        print(year, "is also a Century year")
    else:
        print(year, "is not a Century year")
else:
    print(year, "is not a Leap year")
    if year % 100 == 0:
        print(year, "is a Century year")
    else:
        print(year, "is not a Century year")


# ----- Output -----
# Enter a year: 2000
# 2000 is a Leap year
# 2000 is also a Century year
