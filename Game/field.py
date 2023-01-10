from Game.snake import Snake
import random


class Field:
    def __init__(self, width, length, direction):

        self.length = length
        self.width = width

        self.direction = direction
        self.snake_start = [((self.width / 2), (self.length / 2))]
        self.snake_position = []
        self.snake = Snake()

        self.food_position = []

    def get_random_food_position(self):

        free_pos = []
        for x in range(self.width):
            for y in range(self.length):
                if (x, y) not in self.snake_position:
                    free_pos.append((x, y))
        return random.choice(free_pos)

    def check_food_eaten(self):

        food = self.get_random_food_position()

        if self.snake_position in food:
            eaten = True
        else:
            eaten = False

        print(eaten, food)

        return eaten
