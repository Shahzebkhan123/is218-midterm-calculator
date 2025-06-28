from app.plugins.add import AddCommand

def test_add_command(monkeypatch, capsys):
    inputs = iter(["5", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    AddCommand().execute()
    out, _ = capsys.readouterr()
    assert "Result: 8.0" in out

def test_add_invalid_input(monkeypatch, capsys):
    inputs = iter(["abc", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    AddCommand().execute()
    out, _ = capsys.readouterr()
    assert "Invalid input! Please enter numeric values." in out