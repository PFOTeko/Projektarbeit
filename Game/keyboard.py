import keyboard


class PressedKey:

    def __init__(self):
        self.pressed_key = None

    def read_keyboard(self):

        while True:
            self.pressed_key = keyboard.read_key()
            print(self.pressed_key)
            break

        return self.pressed_key
