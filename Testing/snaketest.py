import unittest
from Game.snake import Snake


class TestSnake(unittest.TestCase):

    def test_snake_direction(self):

        start_position = [(0, 0), (1, 0), (2, 0)]

        snake = Snake(start_position)

        direction = None

        # Act

        actual_result_direction = snake.set_direction(direction)

        # Assert
        self.assertEqual(actual_result_direction, 'Left')

        print(actual_result_direction)

    def test_snake_grow(self):

        start_position = [(0, 0), (1, 0), (2, 0)]

        snake = Snake(start_position)

        snake.set_direction('Down')

        # Act
        snake.move()
        actual_result_grow = snake.grow()

        # Assert
        self.assertEqual(actual_result_grow, [(0, 1), (0, 0), (1, 0), (2, 0)])

        print(actual_result_grow)

    def test_snake_move(self):

        start_position = [(0, 0), (1, 0), (2, 0)]

        snake = Snake(start_position)

        direction = 'Up'

        snake.set_direction(direction)

        # Act

        actual_result_move = snake.move()

        # Assert
        self.assertEqual(actual_result_move, [(0, -1), (0, 0), (1, 0)])

        print(actual_result_move)


if __name__ == '__main__':
    unittest.main()
