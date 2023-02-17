from Game.snake import Snake
import random


class Field:
    def __init__(self):

        self.start_position = [(0, 0), (1, 0), (2, 0)]
        self.height = 14
        self.width = 14
        self.snake = Snake(self.start_position)
        self.food = []
        self.game_over = False
        self.counter = 0

    def get_random_food_position(self):

        free_pos = []
        for x in range((-1 * self.width), self.width):
            for y in range((-1 * self.height) + 1, self.height - 1):
                if (x, y) not in self.snake.snake_body:
                    free_pos.append((x, y))

        return random.choice(free_pos)

    def check_food_eaten(self):

        if self.food in self.snake.snake_body:
            is_eaten = True
        else:
            is_eaten = False

        return is_eaten

    def build_game(self, direction):

        self.snake.set_direction(direction)
        self.snake.move()

        self.snake.change_side(self.width, self.height)

        if self.food is None or len(self.food) == 0:
            self.food = self.get_random_food_position()

        if self.check_food_eaten():
            self.food = self.get_random_food_position()
            self.snake.grow()
            self.counter += 1

        if self.snake.check_self_crash():
            self.game_over = True

        return self.snake.snake_body