# Question 28: Write a program to calculate discounts based on total shopping amount.

amount = float(input("Enter total shopping amount: "))

if amount >= 5000:
    discount = amount * 0.20
elif amount >= 3000:
    discount = amount * 0.10
elif amount >= 1000:
    discount = amount * 0.05
else:
    discount = 0

final_amount = amount - discount
print("Discount: Rs.", discount)
print("Final amount to pay: Rs.", final_amount)


# ----- Output -----
# Enter total shopping amount: 3500
# Discount: Rs. 350.0
# Final amount to pay: Rs. 3150.0
