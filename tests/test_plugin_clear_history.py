import os
import pandas as pd
from app.history import HistoryManager
from app.plugins.clear_history import ClearHistoryCommand

def test_clear_history(capsys):
    # Save a dummy entry first
    HistoryManager().save("test", 1, 1, 2)

    cmd = ClearHistoryCommand()
    cmd.execute()

    out, _ = capsys.readouterr()
    assert "History cleared." in out

    df = pd.read_csv("data/history.csv")
    assert df.empty
