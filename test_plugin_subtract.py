from app.plugins.subtract import SubtractCommand
import builtins

def test_subtract_command(monkeypatch, capsys):
    inputs = iter(["7", "2"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    cmd = SubtractCommand()
    cmd.execute()

    out, _ = capsys.readouterr()
    assert "Result: 5.0" in out
