class Snake:

    def __init__(self, start_position):

        self.snake_body = start_position
        self.direction = 'Left'
        self.moves = {'Up': (0, -1), 'Down': (0, 1), 'Left': (-1, 0), 'Right': (1, 0)}
        self.tail = []
        self.directions = ['Up', 'Down', 'Right', 'Left']

    def set_direction(self, direction):

        if direction in self.directions:
            self.direction = direction

        return self.direction

    def move(self):

        x, y = self.snake_body[0]
        dx, dy = self.moves[self.direction]
        new_head_position = x + dx, y + dy

        self.snake_body.insert(0, new_head_position)
        self.tail = self.snake_body.pop()

        return self.snake_body

    def grow(self):

        self.snake_body.append(self.tail)

        return self.snake_body

    def check_self_crash(self):

        snake_body = self.snake_body.copy()

        snake_body.pop(0)

        if self.snake_body[0] in snake_body:
            bite = True
        else:
            bite = False

        return bite
