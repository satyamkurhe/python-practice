# Question 47: Write a program to check user role (admin, user, guest) using match case.

role = input("Enter role (admin/user/guest): ").lower()

match role:
    case "admin":
        print("Full access: can add, edit and delete data")
    case "user":
        print("Limited access: can view and edit own data")
    case "guest":
        print("Read-only access")
    case _:
        print("Unknown role")


# ----- Output -----
# Enter role (admin/user/guest): admin
# Full access: can add, edit and delete data
