from Game.snake import Snake
import random


class Field:
    def __init__(self, width, height, direction):

        self.height_field = height
        self.width_field = width
        self.direction = direction
        self.snake_start = [((self.width_field / 2), (self.height_field / 2))]
        self.snake = Snake()
        self.snake_position = []
        self.food = []

    def get_random_food_position(self):

        free_pos = []
        for x in range(self.width_field):
            for y in range(self.height_field):
                if (x, y) not in self.snake:
                    free_pos.append((x, y))
        return random.choice(free_pos)

    def place_objects(self):

        self.food = self.get_random_food_position()
        self.snake_position = self.snake.move_snake(self.direction)

        return self.food, self.snake_position

    def check_food_eaten(self):

        if self.snake_position in self.food:
            eaten = True
        else:
            eaten = False

        return eaten
