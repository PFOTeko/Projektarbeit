from field import Field
from gui import Gui

from observer import Observer


class Controller(Observer):

    def __init__(self):
        self.gui = Gui()
        self.model = Field(8,8,8,1)

        self.gui.attach(self)

        self.gui.run()

    def update(self):
        print("foo")

    def model(self):

        print('Hallo Welt')

    def pressed(self, event):
        pressed = event.keysym
        keys = ['Up', 'Down', 'Right', 'Left']

        if pressed in keys:
            Controller.model(pressed)
            print(event.keysym)


if __name__ == "__main__":
    start = Controller()



