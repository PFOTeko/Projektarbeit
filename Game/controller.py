from field import Field
from gui import Gui
from observer import Observer

import time


class Controller(Observer):

    def __init__(self, model: Field, view: Gui):

        self.field = model
        self.gui = view

        self.gui.attach(self)

        self.snake = self.field.build_game(None)

        self.gui.draw_snake(self.snake)
        self.gui.draw_food(self.field.food)

        self.pressed = None
        self.speed = 0.3
        self.loop = True
        self.pause = False

    def update(self, event):

        button = ['restart', 'pause', 'speed_up', 'speed_down']

        if event in button:

            if event == 'speed_up' or 'speed_down':
                self.get_speed(event)

            if event == 'pause':
                self.pause = not self.pause

            if event == 'restart':
                self.restart()

            if event == 'exit':
                self.loop ^= self.loop

        else:
            self.pressed = event.keysym

    def get_speed(self, change):

        if change == 'speed_up':
            self.speed -= 0.05
            if self.speed <= 0:
                self.speed = 0.05

        if change == 'speed_down':
            self.speed += 0.05

    def update_game(self):

        self.snake = self.field.build_game(self.pressed)

        self.gui.clean_canvas()
        self.gui.draw_food(self.field.food)
        self.gui.draw_snake(self.snake)
        self.gui.draw_score(self.field.counter)

        if self.field.game_over:
            self.gui.draw_game_over()

    def run(self):

        start_time = time.time()

        while self.loop:

            delta_time = round((time.time() - start_time), 4)

            if delta_time >= self.speed:

                if not self.pause and not self.field.game_over:
                    self.update_game()

                self.gui.update()

                print(self.pause)
                print(self.speed)
                start_time = time.time()
    def restart(self):
        print('restart')


if __name__ == "__main__":

    model = Field()
    view = Gui()
    controller = Controller(model, view)

    controller.run()

