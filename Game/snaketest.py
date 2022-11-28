import unittest

from snake import Snake


class TestSnake(unittest.TestCase):

    def test_snake(self):

        snake = Snake()

        # Act
        actual_result = snake.move_snake('up', True)

        # Assert
        self.assertTrue(actual_result)


if __name__ == '__main__':
    unittest.main()
