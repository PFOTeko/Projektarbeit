
class Snake:

    def __init__(self):

        self.snake_body = [(0, 0)]
        # self.head = Head()
        self.direction = None
        self.moves = {'up': (0, -1), 'down': (0, 1), 'left': (-1, 0), 'right': (1, 0)}
        self.movement = None

    def move_snake(self, direction):

        '''gib neue Kopfposition zurueck
           direction: 'up', 'down',...
        '''

        x, y = self.snake_body[0]
        dx, dy = self.moves[direction]
        new_head_position = x + dx, y + dy

        return new_head_position != self.snake_body[0]






















