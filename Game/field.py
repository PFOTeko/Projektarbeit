from snake import Snake
import random


class Field:
    def __init__(self, width, length, size, direction):

        self.length = length
        self.width = width
        self.direction = direction
        self.snake_position = [((self.width/2), (self.length/2))]
        self.snake = Snake()
        self.eaten = None
        self.food = []
        self.size = size

    def food_position(self):
        free_pos = []
        for x in range(self.width):
            for y in range(self.length):
                if (x, y) not in self.snake_position:
                    free_pos.append((x, y))

        self.food = random.choice(free_pos)
        return self.food

    def offset_snake(self):

        xy, s = self.snake.move_snake(self.direction, False)

        for n in xy:

            x, y = n
            dx = (self.size*x)
            dy = (self.size*y)

            print(dx, dy)

        print(s)

    def playing_field(self):

        self.offset_snake()
        #self.food_position()

        #print(self.food, self.snake.move_snake(self.direction, False))

        return
















        









