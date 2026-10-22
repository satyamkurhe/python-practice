# Question 44: Write a program to check traffic signal actions using match case.

signal = input("Enter traffic signal color (red/yellow/green): ").lower()

match signal:
    case "red":
        print("Stop")
    case "yellow":
        print("Get ready")
    case "green":
        print("Go")
    case _:
        print("Invalid signal color")


# ----- Output -----
# Enter traffic signal color (red/yellow/green): red
# Stop
