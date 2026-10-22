# Question 45: Print numbers skipping multiples of 3.

# Print numbers from 1 to 20, skipping multiples of 3
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i, end=" ")
print()


# ----- Output -----
# 1 2 4 5 7 8 10 11 13 14 16 17 19 20
