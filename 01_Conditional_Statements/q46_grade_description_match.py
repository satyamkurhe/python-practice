# Question 46: Write a program to print grade description using match case.

grade = input("Enter grade (A/B/C/D/F): ").upper()

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Very Good")
    case "C":
        print("Good")
    case "D":
        print("Satisfactory")
    case "F":
        print("Fail - Try again")
    case _:
        print("Invalid grade")


# ----- Output -----
# Enter grade (A/B/C/D/F): B
# Very Good
