import sys

class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
    
    def modulus(self, a, b):
        return a % b


def main():
    calc = Calculator()
    continue_calculations = True
    previous_result = 0
    is_first_calculation = True
    
    while continue_calculations:
        if is_first_calculation:
            try:
                a = float(input("Enter the first number:\n"))
                is_first_calculation = False
            except ValueError:
                print("Please enter a valid number.")
                continue
        else:
            a = previous_result
            print(f"Using previous result: {a}")
        
        try:
            b = float(input("Enter the second number:\n"))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        operation_symbol = input("Enter operation symbol (+, -, *, /, %):\n").strip()
        
        operations = {
            "+": calc.add,
            "-": calc.subtract,
            "*": calc.multiply,
            "/": calc.divide,
            "%": calc.modulus
        }
        
        operation = operations.get(operation_symbol)
        
        if operation is None:
            print("Entered operation is not valid.")
            continue
        
        try:
            previous_result = operation(a, b)
            print(f"Result: {previous_result}")
        except ZeroDivisionError as ex:
            print(str(ex))
            continue
        
        continue_response = input("Perform another calculation using this result? (yes/no):\n").strip().lower()
        continue_calculations = continue_response in ["yes", "y"]


if __name__ == "__main__":
    main()