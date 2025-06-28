from app.plugins.divide import DivideCommand

def test_divide_command(monkeypatch, capsys):
    inputs = iter(["10", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    cmd = DivideCommand()
    cmd.execute()

    out, _ = capsys.readouterr()
    assert "Result: 5.0" in out

def test_divide_by_zero(monkeypatch, capsys):
    inputs = iter(["10", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    cmd = DivideCommand()
    cmd.execute()

    out, _ = capsys.readouterr()
    assert "Error: Cannot divide by zero!" in out

