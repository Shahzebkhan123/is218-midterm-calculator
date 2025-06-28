import pytest
from app import App

def test_get_environment_variable():
    app = App()
    assert app.get_environment_variable("NON_EXISTENT_VAR") == "DEVELOPMENT"

def test_exit_command(monkeypatch):
    app = App()
    monkeypatch.setattr("builtins.input", lambda _: "exit")
    with pytest.raises(SystemExit):
        app.start()
