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

        button = ['start', 'pause', 'speed_up', 'speed_down']
        keys = ['Up', 'Down', 'Right', 'Left']

        if event in button:
            print(event)
        else:
            pressed = event.keysym
            if pressed in keys:
                print(pressed)


if __name__ == "__main__":
    start = Controller()



