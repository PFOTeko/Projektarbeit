from Game.snake import Snake
import random


class Field:
    def __init__(self, width, length, size, direction):

        self.length = length
        self.width = width
        self.size = size

        self.direction = direction
        self.snake_start = [((self.width / 2), (self.length / 2))]
        self.snake_position = []
        self.snake = Snake()

        self.eaten = None
        self.food_position = []
        self.crash = None

    # todo: Skalierung des Food muss in die View'
    def get_random_food_position(self):

        free_pos = []
        for x in range(self.width):
            for y in range(self.length):
                if (x, y) not in self.snake_position:
                    free_pos.append((x, y))
        return random.choice(free_pos)

    # todo: Skalierung der Schlange muss in die View'

    '''
    def offset_snake(self):

        snake, self.crash = self.snake.move_snake(self.direction, self.eaten)
        offset_x, offset_y = self.snake_start[0]
        offset_snake = []

        for bodyPart in snake:
            x, y = bodyPart

            dx = (self.size * x) + offset_x
            dy = (self.size * y) + offset_y
            new_position = dx, dy

            offset_snake.append(new_position)

        self.snake_position = offset_snake

    # todo: Skalierung (offset_snake) der Schlange muss in die View'
    # todo: rename der Funktion
    
    '''

    def playing_field(self):

        self.get_random_food_position()

        if self.snake_position in self.food_position:
            self.eaten = True

        else:
            self.eaten = False

        print(self.get_random_food_position(), self.snake_position)

        return
