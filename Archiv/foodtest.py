import unittest

from Archiv.food import Food


class TestFood(unittest.TestCase):

    def test_food(self):

        snake_body = [(0, 0), (1, 0), (2, 0)]

        food = Food()

        # Act
        actual_result = food.food_position(10, 10, snake_body)

        # Assert
        self.assertTrue(actual_result)


if __name__ == '__main__':
    unittest.main()
