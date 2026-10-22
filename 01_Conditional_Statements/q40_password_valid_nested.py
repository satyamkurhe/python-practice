# Question 40: Write a program to check whether a password is valid using nested if.

password = input("Enter a password: ")

# Rules: minimum 8 characters, at least one digit, at least one uppercase letter
if len(password) >= 8:
    has_digit = any(ch.isdigit() for ch in password)
    if has_digit:
        has_upper = any(ch.isupper() for ch in password)
        if has_upper:
            print("Password is valid")
        else:
            print("Password must contain at least one uppercase letter")
    else:
        print("Password must contain at least one digit")
else:
    print("Password must be at least 8 characters long")


# ----- Output -----
# Enter a password: Python123
# Password is valid
