from app.commands import Command
from app import command_handler_instance

class MenuCommand(Command):
    def execute(self):
        print("Available commands:")
        for cmd_name in command_handler_instance.commands:
            print(f" - {cmd_name}")
