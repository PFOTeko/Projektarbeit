from Game import gui
from Game import field


class Controller:

    def __init__(self):
        self.gui = gui.Gui()
        self.gui.register_callback(self.gui_callbacks)

        #self.field = field.Field()


    def start_gui(self):
        self.gui.show_window()

    def gui_callbacks(self, event, data):
        print("gui_callbacks: " + str(event))

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
    start.start_gui()
