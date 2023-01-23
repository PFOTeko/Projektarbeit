from Game.snake import Snake
import random


class Field:
    def __init__(self):

        self.height_field = 29
        self.width_field = 29
        self.snake_start = [((self.width_field / 2), (self.height_field / 2))]
        self.snake = Snake()
        self.snake_position = []
        self.food = []
        self.game_over = False
        self.counter = 0

    def get_snake(self, direction):

        self.snake_position = self.snake.move_snake(direction)

        return self.snake_position

    def get_random_food_position(self):

        free_pos = []
        for x in range(self.width_field):
            for y in range(self.height_field):
                if (x, y) not in self.snake_position:
                    free_pos.append((x, y))

        return random.choice(free_pos)

    def check_food_eaten(self):

        if self.food in self.snake_position:
            eaten = True
        else:
            eaten = False

        return eaten

    def build_game(self, direction):

        snake = self.get_snake(direction)

        if self.food is None or len(self.food) == 0:
            self.food = self.get_random_food_position()

        eaten = self.check_food_eaten()

        if eaten is True:
            self.food = self.get_random_food_position()
            self.snake.grow_snake()
            self.counter += 1

        crash = self.snake.check_self_crash()

        if crash is True:
            self.game_over = True

        return snake, self.food, self.counter, self.game_over









