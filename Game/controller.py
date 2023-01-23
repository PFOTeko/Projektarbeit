from field import Field
from gui import Gui
from observer import Observer


class Controller(Observer):

    def __init__(self):

        self.field = Field()
        self.snake, self.food, self.counter, self.game_over = self.field.build_game('Left')

        self.gui = Gui()
        self.gui.draw_snake(self.snake)
        self.gui.draw_food(self.food)

        self.gui.attach(self)
        self.gui.run()

    def update(self, event):

        button = ['start', 'pause', 'speed_up', 'speed_down']
        keys = ['Up', 'Down', 'Right', 'Left']

        if event in button:
            print('Button')

        else:
            pressed = event.keysym
            if pressed in keys:
                self.update_game(pressed)

    def update_game(self, direction):

        self.snake, self.food, self.counter, self.game_over = self.field.build_game(direction)

        self.gui.clean_canvas()
        self.gui.draw_food(self.food)
        self.gui.draw_snake(self.snake)
        self.gui.draw_score(self.counter)

        print(self.snake, self.food, self.counter, self.game_over)


if __name__ == "__main__":
    start = Controller()



