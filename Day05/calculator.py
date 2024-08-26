import sys
import os

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2


# Convert arguments to integers
num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

print(sys.argv)
if operation == "add":
    print(add(num1, num2))
elif operation == "sub":
    print(sub(num1, num2))
elif operation == "mul":
    print(mul(num1, num2))
else:
    print("Your input is incorrect")
    



password = os.getenv("password")
print(password)