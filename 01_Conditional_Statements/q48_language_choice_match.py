# Question 48: Write a program to print language choice using match case.

print("Choose your language:")
print("1. English")
print("2. Marathi")
print("3. Hindi")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Hello! Welcome")
    case 2:
        print("नमस्कार! स्वागत आहे")
    case 3:
        print("नमस्ते! स्वागत है")
    case _:
        print("Invalid choice")


# ----- Output -----
# Choose your language:
# 1. English
# 2. Marathi
# 3. Hindi
# Enter your choice: 2
# नमस्कार! स्वागत आहे
