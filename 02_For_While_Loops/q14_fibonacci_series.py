# Question 14: Print Fibonacci series up to n terms.

n = int(input("Enter number of terms: "))
a = 0
b = 1

print("Fibonacci series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()


# ----- Output -----
# Enter number of terms: 10
# Fibonacci series:
# 0 1 1 2 3 5 8 13 21 34
