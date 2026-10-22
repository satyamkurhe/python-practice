# Question 22: Write a program to check salary bonus based on years of service.

years = int(input("Enter years of service: "))

if years >= 10:
    bonus = 20000
elif years >= 5:
    bonus = 10000
elif years >= 2:
    bonus = 5000
else:
    bonus = 0

print("Bonus amount: Rs.", bonus)


# ----- Output -----
# Enter years of service: 6
# Bonus amount: Rs. 10000
