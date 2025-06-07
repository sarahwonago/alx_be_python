def perform_operation(num1, num2, operation):
    if operation == 'divide' and (num1 == 0 or num2== 0):
        return "Cannot divide by zero."
    match operation:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            return num1 / num2


