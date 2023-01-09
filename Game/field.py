from snake import Snake
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

        if self.eaten is None or True:
            free_pos = []
            for x in range(self.width):
                n = x // self.size
                x = n * self.size
                for y in range(self.length):
                    i = y // self.size
                    y = i * self.size
                    if (x, y) not in self.snake_position:
                        free_pos.append((x, y))
            self.food_position = random.choice(free_pos)

    # todo: Skalierung der Schlange muss in die View'

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
    def playing_field(self):

        self.food()

        if self.snake_position in self.food_position:
            self.eaten = True
            self.offset_snake()
        else:
            self.eaten = False
            self.offset_snake()

        print(self.food_position, self.snake_position, self.crash)

        return
