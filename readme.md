Advanced Calculator 📊
📌 Project Overview
This project is a Python-based calculator that supports:

✅ Addition, Subtraction, Multiplication, and Division
✅ History tracking of past calculations
✅ Exception handling for division by zero
✅ Object-Oriented Programming (OOP) principles
✅ Full unit testing with pytest
✅ 100% Pylint-compliant code
This project is designed to demonstrate best practices in Python, including static methods, class methods, exception handling, and unit testing.

📌 Technologies Used
Python 🐍 (Version 3.9+)
Decimal Module (For precise calculations)
Pytest (For unit testing)
Pylint (For code quality checks)
📌 Project Structure
calculator_project/
│── calculator/
│   ├── __init__.py
│   ├── operations.py         # Arithmetic functions (add, subtract, multiply, divide)
│   ├── calculation.py        # Stores a single calculation
│   ├── calculations.py       # Manages calculation history
│── tests/
│   ├── test_calculation.py   # Tests for Calculation 
│   ├── test_calculator.py    # Tests for Calculator class
│   ├── test_calculations.py    # Tests for Calculations classes
│   ├── test_operations.py    # Tests for operations class
│── README.md                 # Project documentation
│── requirements.txt          # List of dependencies
│── pytest.ini                # Pytest configuration
│── .pylintrc                 # Pylint configuration

📌 Installation & Setup
🔹 Step 1: Clone the Repository
git clone https://github.com/askanade18/IS-601-Advanced_Calculator.git
cd calculator

🔹 Step 2: Create a Virtual Environment (Optional but Recommended)

python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows

🔹 Step 3: Install Dependencies
pip install -r requirements.txt

📌 Usage
🔹 Import and Use the Calculator
from calculator.calculator import Calculator

# Perform calculations
print(Calculator.add(10, 5))        # Output: 15
print(Calculator.subtract(10, 5))   # Output: 5
print(Calculator.multiply(10, 5))   # Output: 50
print(Calculator.divide(10, 2))     # Output: 5.0

# Handling division by zero
try:
    Calculator.divide(10, 0)
except ValueError as e:
    print(e)  # Output: Cannot divide by zero
🔹 View Calculation History
from calculator.calculations import Calculations

print(Calculations.get_history())  # Get all calculations
print(Calculations.get_latest())   # Get the last calculation
Calculations.clear_history()       # Clear calculation history

📌 Running Unit Tests 🧪
Run All Tests
pytest
Check Test Coverage
pytest --cov=calculator
📌 Code Quality Check ✅
Run Pylint
pylint calculator

