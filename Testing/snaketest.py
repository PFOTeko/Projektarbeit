import unittest
from Game.snake import Snake


class TestSnake(unittest.TestCase):

    def test_snake_direction(self):

        start_position = [(0, 0), (1, 0), (2, 0)]

        snake = Snake(start_position)

        direction = 'Up'

        # Act

        actual_result_move = snake.move(direction)

        # Assert
        self.assertEqual(actual_result_move, [(0, -1), (0, 0), (1, 0)])

        print(actual_result_move)

    def test_snake_grow(self):

        start_position = [(0, 0), (1, 0), (2, 0)]

        snake = Snake(start_position)

        # Act
        snake.move('Down')
        actual_result_grow = snake.grow()

        # Assert
        self.assertEqual(actual_result_grow, [(0, 1), (0, 0), (1, 0), (2, 0)])

        print(actual_result_grow)

    def test_snake_move(self):

        start_position = [(0, 0), (1, 0), (2, 0)]

        snake = Snake(start_position)

        # Act

        actual_result_move = snake.check_direction()

        # Assert
        self.assertEqual(actual_result_move, [(-1, 0), (0, 0), (1, 0)])

        print(actual_result_move)




if __name__ == '__main__':
    unittest.main()
