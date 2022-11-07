import unittest

from  Testing import snake

class TestCrashing(unittest.TestCase):

    def test_crash(self):
        # Arrange
        position1 = 2 , 5
        position2 = 2 , 5

        # Act
        actual_result = snake.crash(position1, position2)

        # Assert
        self.assertTrue(actual_result)


if __name__ == '__main__':
    unittest.main()
