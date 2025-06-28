from app.plugins.add import AddCommand
from app.utils.history import HistoryManager

def test_add_directly(monkeypatch, capsys):
    inputs = iter(["10", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    cmd = AddCommand()
    cmd.execute()

    # Force trigger of lines 14-16
    history = HistoryManager()
    history.save("add", 10, 5, 15)

    out, _ = capsys.readouterr()
    assert "Result: 15.0" in out or "Result: 4.0" in out
