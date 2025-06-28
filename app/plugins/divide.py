import logging
from app.commands import Command
from app.history import HistoryManager

class DivideCommand(Command):
    def execute(self):
        try:
            num1 = float(input("Enter numerator: "))
            num2 = float(input("Enter denominator: "))
            if num2 == 0:
                print("Error: Cannot divide by zero!")
                logging.warning("Attempted division by zero")
                return
            result = num1 / num2
            print(f"Result: {result}")
            HistoryManager().save("divide", num1, num2, result)
            logging.info(f"Division: {num1} / {num2} = {result}")
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            logging.error("Invalid input in DivideCommand")
