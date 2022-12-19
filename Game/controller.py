import gui
import field
from observer import Observer


class Controller(Observer):

    def __init__(self):
        self.gui = gui.Gui()
        self.model = field()

        self.view.attche(self)

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



