from Game.snake import Snake
import random


class Field:
    def __init__(self, width, length, direction):

        self.length = length
        self.width = width
        self.direction = direction
        self.snake_start = [((self.width / 2), (self.length / 2))]
        self.snake = Snake()
        self.snake_position = []
        self.food = []

    def get_random_food_position(self):

        free_pos = []
        for x in range(self.width):
            for y in range(self.length):
                if (x, y) not in self.snake_position:
                    free_pos.append((x, y))
        return random.choice(free_pos)

    def palce_objects(self):

        self.food = self.get_random_food_position()
        self.snake_position = self.snake.move_snake(self.direction)

        return self.food, self.snake_position

    def check_food_eaten(self):

        if self.snake_position in self.food:
            eaten = True
        else:
            eaten = False

        return eaten


