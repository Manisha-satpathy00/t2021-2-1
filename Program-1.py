class Calculator:
    def _init_(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def calculate(self):
        if self.operation == 'addition':
            return self.a + self.b
        elif self.operation == 'subtraction':
            return self.a - self.b
        elif self.operation == 'multiplication':
            return self.a * self.b
        elif self.operation == 'division':
            if self.b != 0:
                return self.a / self.b
            else:
                return 'Error: Cannot divide by zero.'
        else:
            return 'Error: Invalid operation.'

# Example usage:
a = 5.0
b = 3.0
operation = 'division'

calc = Calculator(a, b, operation)
result = calc.calculate()
print(f"The result of {operation} is: {result}")
