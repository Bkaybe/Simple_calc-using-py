def calculator():
    operation = input("Please enter an operation (+, -, *, /): ")
    num1 = float(input("Please enter the first number: "))
    num2 = float(input("Please enter the second number: "))

    if operation == '+':
        print(num1 + num2)
    elif operation == '-':
        print(num1 - num2)
    elif operation == '*':
        print(num1 * num2)
    elif operation == '/':
        print(num1 / num2)
    else:
        print("Invalid operator")

calculator()