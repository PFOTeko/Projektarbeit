class Snake:

    def __init__(self):

        self.snake_body = [(0, 0), (1, 0), (2, 0)]
        self.direction = None
        self.moves = {'Up': (0, -1), 'Down': (0, 1), 'Left': (-1, 0), 'Right': (1, 0)}
        self.tail = []

    def move_snake(self, direction):

        x, y = self.snake_body[0]
        dx, dy = self.moves[direction]
        new_head_position = x + dx, y + dy

        self.snake_body.insert(0, new_head_position)
        self.tail = self.snake_body.pop()

        return self.snake_body

    def grow_snake(self):

        self.snake_body.append(self.tail)

        return self.snake_body.append

    def check_self_crash(self):

        if self.snake_body[0] in self.snake_body:
            bitten = True
        else:
            bitten = False

        return bitten