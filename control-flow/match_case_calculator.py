# match_case_calculator.py

# Prompt for first number
num1 = float(input("Enter the first number: "))

# Prompt for second number
num2 = float(input("Enter the second number: "))

# Prompt for operation
operation = input("Choose the operation (+, -, *, /): ")

# Perform calculation using match-case
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")
    case "-":
        result = num1 - num2
        print(f"The result is {result}.")
    case "*":
        result = num1 * num2
        print(f"The result is {result}.")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")
    case _:
        print("Invalid operation selected.")
