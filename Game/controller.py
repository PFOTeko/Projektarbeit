from field import Field
from gui import Gui
from observer import Observer

import time


class Controller(Observer):

    def __init__(self, model: Field, view: Gui):

        self.field = model
        self.gui = view

        self.gui.attach(self)

        self.snake, self.food, self.counter, self.game_over = self.field.build_game(None)

        self.gui.draw_snake(self.snake)
        self.gui.draw_food(self.food)

        self.pressed = None

    def update(self, event):

        button = ['start', 'pause', 'speed_up', 'speed_down']
        keys = ['Up', 'Down', 'Right', 'Left']

        if event in button:
            print('Button')

        else:
            self.pressed = event.keysym

    def update_game(self):

        self.snake, self.food, self.counter, self.game_over = self.field.build_game(self.pressed)

        self.gui.clean_canvas()
        self.gui.draw_food(self.food)
        self.gui.draw_snake(self.snake)
        self.gui.draw_score(self.counter)

        print(self.snake, self.food, self.counter, self.game_over)

    def run(self):
        start_time = time.time()
        while True:
            delta_time = round((time.time() - start_time), 2)
            if delta_time > 0.25:
                self.update_game()
                self.gui.update()
                print(delta_time)
                start_time = time.time()


if __name__ == "__main__":

    model = Field()
    view = Gui()
    controller = Controller(model, view)

    controller.run()

