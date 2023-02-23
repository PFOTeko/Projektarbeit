from Game.snake import Snake
import random


class Field:
    def __init__(self):

        self.start_position = None
        self.height = 20
        self.width = 20
        self.food = []
        self.is_game_over = None
        self.counter = None
        self.special_food = []
        self.is_special_food = None
        self.step = None
        self.count = None
        self.snake = None
        self.new_game()

    def new_game(self):

        self.start_position = [(0, 0), (1, 0), (2, 0)]
        self.snake = Snake(self.start_position)
        self.counter = 0
        self.step = 0
        self.count = 0

        self.food = self.get_random_food_position()
        self.is_game_over = False
        self.is_special_food = False

    def get_random_food_position(self):

        free_pos = []
        for x in range((-1 * self.width) + 1, self.width - 1):
            for y in range((-1 * self.height) + 1, self.height - 1):
                if (x, y) not in self.snake.body:
                    free_pos.append((x, y))

        return random.choice(free_pos)

    def place_food(self):

        if self.food is None or len(self.food) == 0:
            self.food = self.get_random_food_position()

    def place_special_food(self):

        if self.counter % 5 == 0 and self.counter > 1 and self.is_special_food is False and self.count != self.counter:
            self.count = self.counter
            self.is_special_food = True
            self.step = 0
            self.special_food = self.get_random_food_position()

    def check_eaten_food(self):

        if self.food == self.snake.body[0]:
            self.food = self.get_random_food_position()
            self.snake.grow()
            self.counter += 1

    def check_eaten_special_food(self):

        if self.special_food == self.snake.body[0]:
            self.is_special_food = False
            self.snake.grow()
            self.counter += 2

        if self.step >= 30:
            self.is_special_food = False

    def game_logic(self, direction):

        self.step += 1

        self.place_food()
        self.place_special_food()

        self.snake.change_side(self.width, self.height)
        self.snake.move(direction)

        self.check_eaten_food()
        self.check_eaten_special_food()

        if self.snake.check_self_crash():
            self.is_game_over = True

        return self.snake.body
