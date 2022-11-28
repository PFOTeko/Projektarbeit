import unittest

from control import PressedKey


class TestFood(unittest.TestCase):

    def test_keyboard(self):

        keyboard = PressedKey()

        # Act
        actual_result = keyboard.read_keyboard()

        # Assert
        self.assertTrue(actual_result)


if __name__ == '__main__':
    unittest.main()
