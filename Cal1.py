# Different functions to calculate different operations
def addition(a, b):
    return f"The sum of the two numbers is: {a + b}"

def subtraction(a, b):
    return f"The difference of the two numbers is: {a - b}"

def multiplication(a, b):
    return f"The product of the two numbers is: {a * b}"

def division(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed"
    return f"The division of the two numbers is: {a / b}"

def modulo(a, b):
    return f"The remainder of the two numbers is: {a % b}"

# Function to calculate the result
def calculator():
    try:
        # Get user inputs
        num1 = int(input("Enter first number: "))
        
        # Ensure the user enters a valid operator
        operation = input("Enter any one operation (+, -, *, /, %): ")
        if operation not in ['+', '-', '*', '/', '%']:
            raise ValueError("Invalid operator. Please enter a symbol from (+, -, *, /, %).")
        
        num2 = int(input("Enter second number: "))
        
        # Perform the calculation based on the operation
        match operation:
            case "+":
                return addition(num1, num2)
            case "-":
                return subtraction(num1, num2)
            case "*":
                return multiplication(num1, num2)
            case "/":
                return division(num1, num2)
            case "%":
                return modulo(num1, num2)
    
    except ValueError as e:
        # This catches both invalid number and invalid operator
        return f"Error: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"



# Call calculator function
print(calculator())
