import os
from app.history import HistoryManager
from app.plugins.delete_history import DeleteHistoryCommand

def test_delete_history(capsys):
    # Save a dummy entry first
    HistoryManager().save("test", 1, 1, 2)

    cmd = DeleteHistoryCommand()
    cmd.execute()

    out, _ = capsys.readouterr()
    assert "History file deleted." in out
    assert not os.path.exists("data/history.csv")
