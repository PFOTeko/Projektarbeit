class Snake:

    def __init__(self, start_position):

        self.body = start_position
        self.direction = 'Left'
        self.moves = {'Up': (0, -1), 'Down': (0, 1), 'Left': (-1, 0), 'Right': (1, 0)}
        self.tail = []
        self.directions = ['Up', 'Down', 'Right', 'Left']
        self.restriction = {'Up': 'Down', 'Down': 'Up', 'Left': 'Right', 'Right': 'Left'}
        self.is_change_side_X = False
        self.is_change_side_Y = False

    def set_direction(self, direction):

        restriction = self.restriction[self.direction]

        if not direction == restriction:

            if direction in self.directions:
                self.direction = direction

        return self.direction

    def move(self):

        x, y = self.body[0]
        dx, dy = self.moves[self.direction]
        new_head_position = x + dx, y + dy

        self.body.insert(0, new_head_position)
        self.tail = self.body.pop()

        return self.body

    def change_side(self, width, height):

        up_down = ['Up', 'Down']
        left_right = ['Left', 'Right']

        x, y = self.body[0]

        if self.direction in left_right:

            if x >= width or x <= (width * -1) and not self.is_change_side_X:
                self.body[0] = (x * -1), y
                self.is_change_side_X = True

            else:
                self.is_change_side_X = False

        if self.direction in up_down:

            if y >= height or y <= (height * -1) and not self.is_change_side_Y:
                self.body[0] = x, (y * -1)
                self.is_change_side_Y = True

            else:
                self.is_change_side_Y = False

    def grow(self):

        self.body.append(self.tail)

        return self.body

    def check_self_crash(self):

        body = self.body.copy()

        body.pop(0)

        if self.body[0] in body:
            bite = True
        else:
            bite = False

        return bite
