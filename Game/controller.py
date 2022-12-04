from Game import gui
from Game import field


class Controller:

    def __init__(self):
        self.gui = gui.Gui()
        self.field = field.Field()

    def model(self):
        print('Hallo Welt')

    def pressed(event):
        pressed = event.keysym
        keys = ['Up', 'Down', 'Right', 'Left']

        if pressed in keys:
            Controller.model(pressed)
            print(event.keysym)


if __name__ == "__main__":
    start = Controller()
