import unittest
from Game.field import Field


class TestField(unittest.TestCase):

    def creat_field(self):

        width = 29
        length = 29

        # Creating a test playfield

        expected_result = []

        for x in range(width):
            for y in range(length):
                expected_result.append((x, y))

        return expected_result

    def test_food(self):

        expected_result = self.creat_field()
        field = Field()

        # Act

        food = field.get_random_food_position()

        actual_result_food = food

        # Assert

        self.assertIn(actual_result_food, expected_result)

    def test_build_game(self):

        expected_result_food = self.creat_field()
        field = Field()

        game = field.game_logic(None)

        actual_result_game_snake, actual_result_game_food, counter, game_over = game

        # Assert

        print(actual_result_game_snake)

        expected_result_snake = [(-1, 0), (0, 0), (1, 0)]

        self.assertEqual(actual_result_game_snake, expected_result_snake)
        self.assertIn(actual_result_game_food, expected_result_food)


'''
    def test_check_food_eaten(self):
        Field.snake_position = [1, 2]
        Field.food = [1, 2]
        self.assertTrue(Field.check_food_eaten)

        Field.snake_position = [1, 2]
        Field.food = [3, 4]
        self.assertFalse(Field.check_food_eaten)
'''


if __name__ == '__main__':
    unittest.main()
