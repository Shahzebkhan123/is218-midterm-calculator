from app.commands import Command
from app.history import HistoryManager

class DeleteHistoryCommand(Command):
    def execute(self):
        manager = HistoryManager()
        manager.delete()
        print("History file deleted.")
