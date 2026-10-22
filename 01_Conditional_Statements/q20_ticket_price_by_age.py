# Question 20: Write a program to check ticket price based on age.

age = int(input("Enter age: "))

if age < 5:
    price = 0
elif age <= 12:
    price = 50
elif age < 60:
    price = 100
else:
    price = 60

print("Ticket price: Rs.", price)


# ----- Output -----
# Enter age: 10
# Ticket price: Rs. 50
