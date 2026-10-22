# Question 49: Write a program to print result status using match case.

status = input("Enter result status (pass/fail/absent): ").lower()

match status:
    case "pass":
        print("Congratulations! You have passed the exam")
    case "fail":
        print("Better luck next time. You have failed")
    case "absent":
        print("You were absent for the exam")
    case _:
        print("Invalid status")


# ----- Output -----
# Enter result status (pass/fail/absent): pass
# Congratulations! You have passed the exam
