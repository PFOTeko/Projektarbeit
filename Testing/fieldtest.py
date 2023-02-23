import unittest
from Game.field import Field


class TestField(unittest.TestCase):

    def creat_field(self):

        width = 29
        height = 29

        # Creating a test playfield

        expected_result = []

        for x in range((-1 * width) + 1, width - 1):
            for y in range((-1 * height) + 1, height - 1):
                expected_result.append((x, y))

        return expected_result

    def test_get_random_food(self):

        expected_result = self.creat_field()
        field = Field()

        # Act

        food = field.get_random_food_position()

        actual_result_food = food

        # Assert

        self.assertIn(actual_result_food, expected_result)

    def test_check_eaten_food(self):

        field = Field()
        field.place_food()

        # Act

        field.snake.body[0] = field.food
        field.check_eaten_food()

        actual_result_game_snake = field.counter

        # Assert

        expected_result_snake = 1

        self.assertEqual(actual_result_game_snake, expected_result_snake)

    def test_check_eaten_special_food(self):

        field = Field()
        field.counter = 5
        field.is_special_food = False
        field.place_special_food()

        # Act

        field.snake.body[0] = field.special_food
        field.check_eaten_special_food()

        actual_result_game_snake = field.counter

        # Assert

        expected_result_snake = 7

        self.assertEqual(actual_result_game_snake, expected_result_snake)


if __name__ == '__main__':
    unittest.main()
