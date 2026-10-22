# Question 37: Print numbers until user enters a negative number.

num = int(input("Enter a number (negative to stop): "))

while num >= 0:
    print("You entered:", num)
    num = int(input("Enter a number (negative to stop): "))

print("Negative number entered. Loop stopped.")


# ----- Output -----
# Enter a number (negative to stop): 15
# You entered: 15
# Enter a number (negative to stop): 8
# You entered: 8
# Enter a number (negative to stop): 42
# You entered: 42
# Enter a number (negative to stop): -3
# Negative number entered. Loop stopped.
