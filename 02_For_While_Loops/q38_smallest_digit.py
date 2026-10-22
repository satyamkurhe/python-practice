# Question 38: Find smallest digit in a number.

num = int(input("Enter a number: "))
smallest = 9

while num > 0:
    digit = num % 10
    if digit < smallest:
        smallest = digit
    num = num // 10

print("Smallest digit:", smallest)


# ----- Output -----
# Enter a number: 48251
# Smallest digit: 1
