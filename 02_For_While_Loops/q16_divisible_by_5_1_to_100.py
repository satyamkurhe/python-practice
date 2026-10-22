# Question 16: Print numbers divisible by 5 between 1 and 100.

for i in range(1, 101):
    if i % 5 == 0:
        print(i, end=" ")
print()


# ----- Output -----
# 5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100
