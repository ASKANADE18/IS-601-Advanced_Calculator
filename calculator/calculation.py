class Calculation:
    def __init__(self, num1, num2, operation):
        self.num1 = num1
        self.num2 = num2
        self.operation = operation  # Stores the function reference

    def get_result(self):
        """Executes the stored operation with num1 and num2."""
        return self.operation(self.num1, self.num2)
    