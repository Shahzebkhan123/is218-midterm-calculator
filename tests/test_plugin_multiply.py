from app.plugins.multiply import MultiplyCommand

def test_multiply_command(monkeypatch, capsys):
    inputs = iter(["4", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    MultiplyCommand().execute()
    out, _ = capsys.readouterr()
    assert "Result: 20.0" in out

def test_multiply_invalid_input(monkeypatch, capsys):
    inputs = iter(["abc", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    MultiplyCommand().execute()
    out, _ = capsys.readouterr()
    assert "Invalid input! Please enter numeric values." in out
