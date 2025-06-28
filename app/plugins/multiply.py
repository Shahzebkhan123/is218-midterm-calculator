import logging
from app.commands import Command
from app.history import HistoryManager

class MultiplyCommand(Command):
    def execute(self):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 * num2
            print(f"Result: {result}")
            HistoryManager().save("multiply", num1, num2, result)
            logging.info(f"Multiplication: {num1} * {num2} = {result}")
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            logging.error("Invalid input in MultiplyCommand")
