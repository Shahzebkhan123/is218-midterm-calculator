import logging
import logging.config
import os

env_log_level = os.getenv("LOG_LEVEL", "INFO")

# Load logging config
logging.config.fileConfig("logging.conf", disable_existing_loggers=False)
logging.getLogger().setLevel(env_log_level)

from app.commands import CommandHandler
from app.plugins import load_plugins

# Global handler to be used by all components (like MenuCommand)
command_handler_instance = CommandHandler()
load_plugins(command_handler_instance)

class App:
    def __init__(self):
        self.command_handler = command_handler_instance

    def get_environment_variable(self, var_name):
        import os
        return os.getenv(var_name, "DEVELOPMENT")

    def start(self):
        print("Welcome to the Advanced Python Calculator (type 'exit' to quit)")
        while True:
            user_input = input(">> ").strip().lower()
            if user_input == "exit":
                print("Exiting calculator. Goodbye!")
                raise SystemExit(0)
            self.command_handler.execute_command(user_input)
