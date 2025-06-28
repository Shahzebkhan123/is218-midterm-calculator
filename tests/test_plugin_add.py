from app.plugins.add import AddCommand

def test_add_command(monkeypatch, capsys):
    inputs = iter(["2", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    cmd = AddCommand()
    cmd.execute()

    out, _ = capsys.readouterr()
    assert "Result: 5.0" in out
