from Game.snake import Snake
import random


class Field:
    def __init__(self):

        self.start_position = [(0, 0), (1, 0), (2, 0)]
        self.height_field = 29
        self.width_field = 29
        self.snake_start = [((self.width_field / 2), (self.height_field / 2))]
        self.snake = Snake(self.start_position)
        self.food = []
        self.game_over = False
        self.counter = 0

    def get_random_food_position(self):

        free_pos = []
        for x in range(self.width_field):
            for y in range(self.height_field):
                if (x, y) not in self.snake.snake_body:
                    free_pos.append((x, y))

        return random.choice(free_pos)

    def check_food_eaten(self):

        if self.food in self.snake.snake_body:
            eaten = True
        else:
            eaten = False

        return eaten

    def build_game(self, direction):

        self.snake.set_direction(direction)
        self.snake.move()

        if self.food is None or len(self.food) == 0:
            self.food = self.get_random_food_position()

        eaten = self.check_food_eaten()

        if eaten is True:
            self.food = self.get_random_food_position()
            self.snake.grow()
            self.counter += 1

        crash = self.snake.check_self_crash()

        if crash is True:
            self.game_over = True

        return self.snake.snake_body, self.food, self.counter, self.game_over









