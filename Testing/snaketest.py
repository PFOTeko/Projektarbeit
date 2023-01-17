import unittest
from Game.snake import Snake


class TestSnake(unittest.TestCase):

    def test_snake_move(self):

        snake = Snake()
        snake_body = {'Up': [(0, -1), (0, 0), (1, 0)], 'Down': [(0, 1), (0, 0), (1, 0)], 'Left': [(-1, 0), (0, 0), (1, 0)], 'Right': [(1, 0), (0, 0), (1, 0)]}

        direction = 'Right'

        # Act

        actual_result_move = snake.move_snake(direction)

        # Assert
        self.assertEqual(actual_result_move, snake_body[direction])

        print(actual_result_move)

    def test_snake_grow(self):

        snake = Snake()

        # Act
        snake.move_snake('Down')
        actual_result_grow = snake.grow_snake()

        # Assert
        self.assertEqual(actual_result_grow, [(0, 1), (0, 0), (1, 0), (2, 0)])

        print(actual_result_grow)


if __name__ == '__main__':
    unittest.main()
