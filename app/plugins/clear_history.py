from app.commands import Command
from app.history import HistoryManager

class ClearHistoryCommand(Command):
    def execute(self):
        manager = HistoryManager()
        manager.clear()
        print("History cleared.")
