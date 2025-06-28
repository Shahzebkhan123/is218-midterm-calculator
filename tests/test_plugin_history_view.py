from app.plugins.history_view import HistoryViewCommand
from app.history import HistoryManager
import os
import pandas as pd

def test_history_view_with_data(capsys):
    HistoryManager().save("test", 1, 2, 3)

    cmd = HistoryViewCommand()
    cmd.execute()

    out, _ = capsys.readouterr()
    assert "Calculation History" in out

def test_history_view_no_file(monkeypatch, capsys):
    if os.path.exists("data/history.csv"):
        os.remove("data/history.csv")

    cmd = HistoryViewCommand()
    cmd.execute()

    out, _ = capsys.readouterr()
    assert "No history found." in out
