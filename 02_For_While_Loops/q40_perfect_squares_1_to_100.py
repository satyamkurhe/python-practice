# Question 40: Print numbers which are perfect squares between 1 and 100.

print("Perfect squares between 1 and 100:")

for i in range(1, 101):
    for j in range(1, 11):
        if j * j == i:
            print(i, end=" ")
            break
print()


# ----- Output -----
# Perfect squares between 1 and 100:
# 1 4 9 16 25 36 49 64 81 100
