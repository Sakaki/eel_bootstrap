import eel
from utils.dialog import Dialogs

dialogs = Dialogs()


@eel.expose
def return_hello():
    return "Hello world!!"


@eel.expose
def open_dialog():
    path = dialogs.open_dialog()
    return str(path)


def start_gui():
    eel.init('web')
    eel.start('index.html')


if __name__ == "__main__":
    start_gui()
