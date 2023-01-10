import unittest
from Game.field import Field


class TestField(unittest.TestCase):

    def test_field(self):

        width = 10
        length = 10
        expected_result = []

        for x in range(width):
            for y in range(length):
                expected_result.append((x, y))

        field = Field(width, length, 'Left')

        # Act
        actual_result = field.check_food_eaten()

        # Assert
        self.assertIn(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
