def perform_operation(num1, num2, operation):
    """
    Perform a mathematical operation on two numbers.

    Args:
        num1 (float or int): The first number.
        num2 (float or int): The second number.
        operation (str): The operation to perform ("add", "subtract", "multiply", "divide").

    Returns:
        float or str: The result of the operation, or an error message for invalid cases.
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2
    else:
        return "Invalid operation"
if __name__ == "__main__":
    # Example tests
    print(perform_operation(10, 5, "add"))      # 15
    print(perform_operation(10, 5, "subtract")) # 5
    print(perform_operation(10, 5, "multiply")) # 50
    print(perform_operation(10, 0, "divide"))   # Cannot divide by zero
