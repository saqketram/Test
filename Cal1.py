def calcu(operation, a, b):
    match operation:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            if b == 0:
                return "Error: Division by zero"
            return a / b    
        case '%':
            return a % b
        case _:
            return "Invalid operation"


num1 = int(input("Enter first number: "))
operation = input("Enter operation to calculate: ")
num2 = int(input("Enter second number: "))


result = calcu(operation, num1, num2)
print(num1, operation, num2, "=", result)