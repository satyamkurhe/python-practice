# Question 36: Find sum of numbers entered by user until 0 is entered.

total = 0
num = int(input("Enter a number (0 to stop): "))

while num != 0:
    total = total + num
    num = int(input("Enter a number (0 to stop): "))

print("Sum of entered numbers:", total)


# ----- Output -----
# Enter a number (0 to stop): 10
# Enter a number (0 to stop): 25
# Enter a number (0 to stop): 5
# Enter a number (0 to stop): 40
# Enter a number (0 to stop): 0
# Sum of entered numbers: 80
