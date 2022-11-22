import random


class Food:

    def __init__(self):
        self.new_food_position = []

    def food_position(self, width, height, snake_position):
        free_pos = []
        for x in range(width):
            for y in range(height):
                if (x, y) not in snake_position:
                    free_pos.append((x, y))

        self.new_food_position = random.choice(free_pos)

        print(self.new_food_position)

        return self.new_food_position


