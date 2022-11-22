from snake import Snake


class Field:

    def __init__(self):
        self.length = 400
        self.width = 400
        self.snake_position = ((self.length/2), (self.width/2))
        self.food_position = ((self.length/4), (self.width/4))

        snake = Snake()
