from app import App
import os
from dotenv import load_dotenv

load_dotenv()
env = os.getenv("ENVIRONMENT")
print(f"Environment: {env}")

if __name__ == "__main__":
    app = App()
    app.start()
