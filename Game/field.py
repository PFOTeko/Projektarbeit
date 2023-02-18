from Game.snake import Snake
import random


class Field:
    def __init__(self):

        self.start_position = [(0, 0), (1, 0), (2, 0)]
        self.height = 20
        self.width = 20
        self.snake = Snake(self.start_position)
        self.food = []
        self.game_over = False
        self.counter = 0
        self.special_food = []
        self.is_special_food = False
        self.step = 0
        self.count = 0

    def get_random_food_position(self):

        free_pos = []
        for x in range((-1 * self.width), self.width):
            for y in range((-1 * self.height), self.height):
                if (x, y) not in self.snake.body:
                    free_pos.append((x, y))

        return random.choice(free_pos)

    def check_food(self):

        if self.food is None or len(self.food) == 0:
            self.food = self.get_random_food_position()

        if self.food == self.snake.body[0]:
            self.food = self.get_random_food_position()
            self.snake.grow()
            self.counter += 1

    def check_special_food(self):

        if self.counter % 5 == 0 and self.counter > 1 and self.is_special_food is False and self.count != self.counter:
            self.count = self.counter
            self.is_special_food = True
            self.step = 0
            self.special_food = self.get_random_food_position()

        if self.special_food == self.snake.body[0]:
            self.is_special_food = False
            self.snake.grow()
            self.counter += 2

        if self.step >= 40:
            self.is_special_food = False

    def game_logic(self, direction):

        self.step += 1

        self.snake.set_direction(direction)
        self.snake.move()
        self.snake.change_side(self.width, self.height)

        self.check_food()
        self.check_special_food()

        if self.snake.check_self_crash():
            self.game_over = True

        return self.snake.body
