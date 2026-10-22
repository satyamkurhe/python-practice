# Question 27: Print all factors of a number.

num = int(input("Enter a number: "))

print("Factors of", num, "are:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")
print()


# ----- Output -----
# Enter a number: 36
# Factors of 36 are:
# 1 2 3 4 6 9 12 18 36
