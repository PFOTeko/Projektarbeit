import unittest

from field import Field


class TestField(unittest.TestCase):

    def test_field(self):

        field = Field(400, 400, 20, 'Up')

        # Act
        actual_result = field.playing_field()

        # Assert
        self.assertTrue(actual_result)


if __name__ == '__main__':
    unittest.main()
