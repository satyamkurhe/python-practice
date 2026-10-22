# Question 49: Display menu-driven program using while loop.

while True:
    print()
    print("----- MENU -----")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 4:
        print("Thank you! Exiting program.")
        break

    if choice in (1, 2, 3):
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        if choice == 1:
            print("Sum =", a + b)
        elif choice == 2:
            print("Difference =", a - b)
        else:
            print("Product =", a * b)
    else:
        print("Invalid choice, try again")


# ----- Output -----
#
# ----- MENU -----
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Exit
# Enter your choice: 1
# Enter first number: 10
# Enter second number: 5
# Sum = 15
#
# ----- MENU -----
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Exit
# Enter your choice: 3
# Enter first number: 4
# Enter second number: 3
# Product = 12
#
# ----- MENU -----
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Exit
# Enter your choice: 4
# Thank you! Exiting program.
