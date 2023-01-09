class Snake:

    def __init__(self):

        self.snake_body = [(0, 0), (1, 0), (2, 0)]
        self.direction = None
        self.moves = {'Up': (0, -1), 'Down': (0, 1), 'Left': (-1, 0), 'Right': (1, 0)}
        self.movement = None
        self.bitten = None

    def move_snake(self, direction, eaten):

        # gib neue Kopfposition zurück direction: 'up', 'down',...
        x, y = self.snake_body[0]
        dx, dy = self.moves[direction]
        new_head_position = x + dx, y + dy

        # Körper anpassen, wenn etwas gegessen wird.
        if eaten:
            self.snake_body.insert(0, new_head_position)
        else:
            self.snake_body.insert(0, new_head_position)
            self.snake_body.pop()

        #print(self.snake_body) # Ausgabe der Schlange

        return self.snake_body

    def check_self_crash(self):

        # todo: Überprüfung auf Biss muss in eine neue Funktion
        # Prüfung ob eigener Körper gebissen wurde.
        if new_head_position in self.snake_body:
            self.bitten = False
        else:
            self.bitten = True