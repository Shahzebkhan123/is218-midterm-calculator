from app.plugins.greet import GreetCommand

def test_greet_command(capsys):
    cmd = GreetCommand()
    cmd.execute()

    out, _ = capsys.readouterr()
    assert "Welcome to the Advanced Python Calculator!" in out
