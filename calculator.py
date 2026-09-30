# Calculator Program


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero."
    return a / b


print("Simple Calculator")
print("------------------")

number1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
number2 = float(input("Enter second number: "))

if operator == "+":
    result = add(number1, number2)

elif operator == "-":
    result = subtract(number1, number2)

elif operator == "*":
    result = multiply(number1, number2)

elif operator == "/":
    result = divide(number1, number2)

else:
    result = "Invalid operator."

print("Result:", result)