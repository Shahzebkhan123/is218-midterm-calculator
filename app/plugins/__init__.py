import os
import importlib

def load_plugins(handler):
    plugin_folder = os.path.dirname(__file__)
    for file in os.listdir(plugin_folder):
        if file.endswith(".py") and file != "__init__.py":
            module_name = f"app.plugins.{file[:-3]}"
            module = importlib.import_module(module_name)
            class_name = "".join([word.capitalize() for word in file[:-3].split("_")]) + "Command"
            if hasattr(module, class_name):
                command_class = getattr(module, class_name)
                handler.register_command(file[:-3], command_class())
