# Question 45: Write a program to print menu-based food selection using match case.

print("----- FOOD MENU -----")
print("1. Pizza   - Rs. 250")
print("2. Burger  - Rs. 120")
print("3. Pasta   - Rs. 180")
print("4. Sandwich- Rs. 90")

choice = int(input("Enter your choice (1-4): "))

match choice:
    case 1:
        print("You ordered Pizza. Bill: Rs. 250")
    case 2:
        print("You ordered Burger. Bill: Rs. 120")
    case 3:
        print("You ordered Pasta. Bill: Rs. 180")
    case 4:
        print("You ordered Sandwich. Bill: Rs. 90")
    case _:
        print("Invalid choice")


# ----- Output -----
# ----- FOOD MENU -----
# 1. Pizza   - Rs. 250
# 2. Burger  - Rs. 120
# 3. Pasta   - Rs. 180
# 4. Sandwich- Rs. 90
# Enter your choice (1-4): 2
# You ordered Burger. Bill: Rs. 120
