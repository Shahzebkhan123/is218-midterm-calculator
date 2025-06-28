import logging
from app.commands import Command
from app.history import HistoryManager

class HistoryViewCommand(Command):
    def execute(self):
        manager = HistoryManager()
        df = manager.load()
        if df.empty:
            print("No history found.")
            logging.info("User viewed empty history.")
        else:
            print("Calculation History:")
            print(df)
            logging.info("User viewed full history table.")
