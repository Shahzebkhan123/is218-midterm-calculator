import pandas as pd
import os

class HistoryManager:
    def __init__(self, filename='data/history.csv'):
        self.filename = filename
        self.columns = ['Operation', 'Operand 1', 'Operand 2', 'Result']

    def save(self, operation, num1, num2, result):
        df = pd.DataFrame([[operation, num1, num2, result]], columns=self.columns)
        if os.path.exists(self.filename):
            df.to_csv(self.filename, mode='a', header=False, index=False)
        else:
            df.to_csv(self.filename, mode='w', header=True, index=False)

    def load(self):
        if os.path.exists(self.filename):
            return pd.read_csv(self.filename)
        else:
            return pd.DataFrame(columns=self.columns)

    def clear(self):
        if os.path.exists(self.filename):
            pd.DataFrame(columns=self.columns).to_csv(self.filename, index=False)

    def delete(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)
