from snake import Snake
from food import Food


class Field:
    def __init__(self):

        self.length = None
        self.width = None
        self.snake_position = ((self.width/2), (self.length/2))
        self.food = Food(self.width, self.length, self.snake_position)
        self.snake = Snake()
        self.direction = control()
        self.eaten = None

    def playing_field(self, length, width):
















        









