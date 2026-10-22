# Question 23: Write a program to calculate electricity bill based on units consumed.

units = int(input("Enter units consumed: "))

# First 100 units : Rs.5 per unit
# Next 100 units  : Rs.7 per unit
# Above 200 units : Rs.10 per unit
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = 100 * 5 + (units - 100) * 7
else:
    bill = 100 * 5 + 100 * 7 + (units - 200) * 10

print("Total electricity bill: Rs.", bill)


# ----- Output -----
# Enter units consumed: 250
# Total electricity bill: Rs. 1700
