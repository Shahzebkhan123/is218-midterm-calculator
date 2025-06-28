from app.plugins.subtract import SubtractCommand

def test_subtract_command(monkeypatch, capsys):
    inputs = iter(["10", "4"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    SubtractCommand().execute()
    out, _ = capsys.readouterr()
    assert "Result: 6.0" in out

def test_subtract_invalid_input(monkeypatch, capsys):
    inputs = iter(["abc", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    SubtractCommand().execute()
    out, _ = capsys.readouterr()
    assert "Invalid input! Please enter numeric values." in out