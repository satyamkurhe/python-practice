# Question 18: Print prime numbers between 1 and 50.

print("Prime numbers between 1 and 50:")

for num in range(2, 51):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print()


# ----- Output -----
# Prime numbers between 1 and 50:
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
