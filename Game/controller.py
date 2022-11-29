import gui


class Controller:

    def __init__(self):
        self.view = gui.Gui()
        self.event
        self.model

    def model(self):
        print('Hallo Welt')
        self.model

    def view(self):
        self.view

    def pressed(event):
        pressed = event.keysym
        keys = ['Up', 'Down', 'Right', 'Left']

        if pressed in keys:

            print(event.keysym)


if __name__ == "__main__":
    start = Controller()
