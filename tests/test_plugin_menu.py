from app.plugins.menu import MenuCommand

def test_menu_command(capsys):
    cmd = MenuCommand()
    cmd.execute()

    out, _ = capsys.readouterr()
    assert "Available commands:" in out
