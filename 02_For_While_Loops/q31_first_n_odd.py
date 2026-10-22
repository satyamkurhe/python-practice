# Question 31: Generate first n odd numbers.

n = int(input("Enter n: "))

for i in range(1, n + 1):
    print(2 * i - 1, end=" ")
print()


# ----- Output -----
# Enter n: 8
# 1 3 5 7 9 11 13 15
