class Calculator:
    def calculate(self, a, b, operation):
        if operation == 'addition':
            return a + b
        elif operation == 'subtraction':
            return a - b
        elif operation == 'multiplication':
            return a * b
        elif operation == 'division':
            if b != 0:
                return a / b
            else:
                return "Cannot divide by zero."
        else:
            return "Invalid operation."

calculator = Calculator()

a = float(input("Enter the value of 'a': "))
b = float(input("Enter the value of 'b': "))
operation = input("Enter the type of operation (addition, subtraction, multiplication, division): ")

result = calculator.calculate(a, b, operation)
print("Result:", result)
