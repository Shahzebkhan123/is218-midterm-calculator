from app.plugins.multiply import MultiplyCommand
import builtins

def test_multiply_command(monkeypatch, capsys):
    inputs = iter(["5", "2"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    cmd = MultiplyCommand()
    cmd.execute()

    out, _ = capsys.readouterr()
    assert "Result: 10.0" in out
