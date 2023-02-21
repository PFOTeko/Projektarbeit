from field import Field
from gui import Gui
from observer import Observer

import time


class Controller(Observer):

    def __init__(self, model: Field, view: Gui):

        self.field = model
        self.gui = view
        self.gui.attach(self)
        self.snake = None
        self.pressed = None
        self.speed = None
        self.is_loop = None
        self.is_pause = None
        self.new_game()

    def new_game(self):

        if self.field.is_game_over:
            self.gui.remove_label()

        self.field.new_game()
        self.snake = self.field.game_logic(None)

        self.gui.draw_snake(self.snake)
        self.gui.draw_food(self.field.food, 'red')
        self.speed = 0.12

        self.is_loop = True
        self.is_pause = False

        self.pressed = None
        self.update_game()

    def update(self, event):

        button = ['restart', 'pause', 'speed_up', 'speed_down']

        if event in button:

            if event == 'speed_up' or 'speed_down':
                self.get_speed(event)

            if event == 'pause':
                self.is_pause = not self.is_pause

            if event == 'restart':
                self.new_game()

            if event == 'exit':
                self.is_loop ^= self.is_loop

        else:
            self.pressed = event.keysym

    def get_speed(self, change):

        if change == 'speed_up':
            self.speed -= 0.03
            if self.speed <= 0.03:
                self.speed = 0.03

        if change == 'speed_down':
            self.speed += 0.03

    def update_game(self):

        self.snake = self.field.game_logic(self.pressed)

        self.gui.clean_canvas()
        self.gui.draw_food(self.field.food, 'red')
        self.gui.draw_snake(self.snake)
        self.gui.draw_score(self.field.counter)

        if self.field.is_special_food:
            self.gui.draw_food(self.field.special_food, 'blue')

        print(self.snake)

        if self.field.is_game_over:
            self.gui.draw_game_over()

    def run(self):

        start_time = time.time()

        while self.is_loop:

            delta_time = round((time.time() - start_time), 4)

            if delta_time >= self.speed:

                if not self.is_pause and not self.field.is_game_over:
                    self.update_game()

                self.gui.update()
                self.gui.draw_speed(round(self.speed, 2))

                start_time = time.time()


if __name__ == "__main__":

    model = Field()
    view = Gui()
    controller = Controller(model, view)

    controller.run()

