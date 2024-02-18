
def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Division by zero is not allowed"


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    print(num1, "+", num2, "=", add(num1, num2))
elif operation == "-":
    print(num1, "-", num2, "=", subtract(num1, num2))
elif operation == "*":
    print(num1, "*", num2, "=", multiply(num1, num2))
elif operation == "/":
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid input")