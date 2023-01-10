import unittest
from Game.field import Field


class TestField(unittest.TestCase):

    def test_field(self):

        # Creating a test playfield
        width = 10
        length = 10
        expected_result = []

        for x in range(width):
            for y in range(length):
                expected_result.append((x, y))

        # Direction left and up the coordinate is out of the field and the test fails
        field = Field(width, length, 'Down')

        # Act

        food, snake = field.palce_objects()
        actual_result_food = food

        actual_result_snake = snake

        # Assert

        self.assertIn(actual_result_food, expected_result)

        for xy in actual_result_snake:
            pos = xy
            self.assertIn(pos, expected_result)

        print(actual_result_food, actual_result_snake)


if __name__ == '__main__':
    unittest.main()
