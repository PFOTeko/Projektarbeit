from snake import Snake
from food import Food


class Field:
    def __init__(self):

        self.length = 400
        self.width = 400
        self.snake_position = ((self.width/2), (self.length/2))
        self.food = Food(self.width, self.length, self.snake_position)
        self.snake = Snake()


    def playing_field(self):

        









