from field import Field
from gui import Gui

from observer import Observer


class Controller(Observer):

    def __init__(self):
        self.gui = Gui()
        self.model = Field(8, 8, 'Left')

        self.gui.attach(self)
        self.gui.run()

    def update(self, event):
        pressed = event.keysym
        keys = ['Up', 'Down', 'Right', 'Left']

        print(pressed)

        if pressed in keys:
            print(pressed)


if __name__ == "__main__":
    start = Controller()



