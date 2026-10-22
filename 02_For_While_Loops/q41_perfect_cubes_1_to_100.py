# Question 41: Print numbers which are perfect cubes between 1 and 100

print("Perfect cubes between 1 and 100:")

for i in range(1, 101):
    for j in range(1, 6):
        if j * j * j == i:
            print(i, end=" ")
            break
print()


# ----- Output -----
# Perfect cubes between 1 and 100:
# 1 8 27 64
