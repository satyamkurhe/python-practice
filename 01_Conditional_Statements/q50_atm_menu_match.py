# Question 50: Write a program to build a simple ATM menu using a match case.

balance = 10000

print("----- ATM MENU -----")
print("1. Check Balance")
print("2. Withdraw")
print("3. Deposit")
print("4. Exit")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Your balance is Rs.", balance)
    case 2:
        amount = int(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance = balance - amount
            print("Please collect your cash. Remaining balance: Rs.", balance)
        else:
            print("Insufficient balance")
    case 3:
        amount = int(input("Enter amount to deposit: "))
        balance = balance + amount
        print("Deposit successful. New balance: Rs.", balance)
    case 4:
        print("Thank you for using the ATM")
    case _:
        print("Invalid choice")


# ----- Output -----
# ----- ATM MENU -----
# 1. Check Balance
# 2. Withdraw
# 3. Deposit
# 4. Exit
# Enter your choice: 2
# Enter amount to withdraw: 1500
# Please collect your cash. Remaining balance: Rs. 8500
