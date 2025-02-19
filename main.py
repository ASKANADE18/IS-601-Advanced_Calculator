from decimal import Decimal, InvalidOperation
from calculator import Calculator

def calculate_and_print(a_string, b_string, operation_string):
    """Function to process inputs and print results, handling exceptions."""
    try:
        # Ensure inputs are valid before converting to Decimal
        if not a_string.replace(".", "", 1).isdigit() or not b_string.replace(".", "", 1).isdigit():
            print(f"Invalid number input: {a_string} or {b_string} is not a valid number.")
            return
        
        num1 = Decimal(a_string)
        num2 = Decimal(b_string)

        if operation_string == "add":
            result = Calculator.add(num1, num2)
        elif operation_string == "subtract":
            result = Calculator.subtract(num1, num2)
        elif operation_string == "multiply":
            result = Calculator.multiply(num1, num2)
        elif operation_string == "divide":
            if num2 == Decimal('0'):  # Handle division by zero
                print("An error occurred: Cannot divide by zero")
                return
            result = Calculator.divide(num1, num2)
        else:
            print(f"Unknown operation: {operation_string}")
            return

        print(f"The result of {num1} {operation_string} {num2} is equal to {result}")

    except InvalidOperation:
        print(f"Invalid number input: {a_string} or {b_string} is not a valid number.")

def main():
    """Main entry point for the CLI calculator."""
    print("Welcome to the CLI Calculator. Type 'exit' to quit.")

    while True:
        try:
            a_string = input("Enter first number: ")
            if a_string.lower() == "exit":
                print("Exiting calculator...")
                break

            b_string = input("Enter second number: ")
            if b_string.lower() == "exit":
                print("Exiting calculator...")
                break

            operation_string = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()
            if operation_string == "exit":
                print("Exiting calculator...")
                break

            calculate_and_print(a_string, b_string, operation_string)

        except KeyboardInterrupt:
            print("\nExiting calculator...")
            break

if __name__ == "__main__":
    main()
