import unittest
from Game.field import Field


class TestField(unittest.TestCase):

    def creat_field(self):

        width = 10
        length = 10

        # Creating a test playfield

        expected_result = []

        for x in range(width):
            for y in range(length):
                expected_result.append((x, y))

        return expected_result

    def test_food_and_snake(self):

        width = 10
        length = 10

        expected_result = self.creat_field()
        field = Field(width, length)

        # Act
        # Direction left and up the coordinate is out of the field and the test fails
        snake = field.get_snake('Right')
        #print(snake)
        food = field.get_random_food_position()
        #print(food)
        actual_result_food = food

        actual_result_snake = snake

        # Assert

        self.assertIn(actual_result_food, expected_result)

        for xy in actual_result_snake:
            pos = xy
            self.assertIn(pos, expected_result)

    def test_build_game(self):

        width = 10
        length = 10

        expected_result = self.creat_field()
        field = Field(width, length)

        game = field.build_game('Right')

        actual_result_game_snake, actual_result_game_food = game

        # Assert

        for xy in actual_result_game_snake:
            pos = xy
            self.assertIn(pos, expected_result)

        self.assertIn(actual_result_game_food, expected_result)


if __name__ == '__main__':
    unittest.main()
