# IS218 Midterm Project – Advanced Python Calculator

This project is a command-line calculator built for the IS218 midterm. It follows good software engineering practices like modularity, design patterns, unit testing, and GitHub Actions for automation.

The calculator uses a plugin system where each math operation is built as a separate module. It also includes a history feature using the pandas library, so previous calculations can be saved, viewed, cleared, or deleted.

## What the Calculator Can Do

- Add, subtract, multiply, and divide numbers
- Show calculation history
- Clear the entire history
- Delete a specific row from history
- Use the command design pattern to structure the app
- Load plugins dynamically
- Use pandas to manage and store the history
- Automatically run tests on GitHub with every code update

## How the Project is Organized

├── app/ # Main application files
│ ├── command_handler.py
│ ├── plugins/ # Math operation plugins
│ └── history/ # History functions using pandas
├── tests/ # Unit tests for each plugin and feature
├── requirements.txt # All required Python packages
├── pytest.ini # Configuration for pytest
├── .github/workflows/ # GitHub Actions workflow file
│ └── python-app.yml
├── README.md # This file


## How to Set It Up

1. **Clone the repo**
   ```bash
   git clone https://github.com/Shahzebkhan123/is218-midterm-calculator.git
   cd is218-midterm-calculator

2. Create a virtual environment 
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

3. Install all required packages 

pip install -r requirements.txt

4. Run the calculator 
python main.py

5. Run the tests 

pytest

GitHub Actions Setup

This project uses GitHub Actions to automatically:

Install dependencies
Run unit tests with pytest
Show test results on the GitHub Actions page
The workflow file is located at .github/workflows/python-app.yml.

Notes

This project uses the Command design pattern for better structure.
All plugins are loaded dynamically using importlib.
Pandas is used to store and manage the calculation history.
All code is tested using pytest with test files located in the tests/ folder.
Author

Shahzeb Khan – IS218 Midterm, Summer 2025 
