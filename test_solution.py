import solution
import unittest


class Test_TestSolution(unittest.TestCase):
    def setUp(self):
        self.sut = solution.Solution()

    def test_insert_new(self):
        self.assertEqual(
            self.sut.insert([[1, 2]], [4, 5]),
            [[1, 2], [4, 5]])

    def test_insert_overlapping_one(self):
        self.assertEqual(
            self.sut.insert([[1, 2]], [2, 5]),
            [[1, 5]])

    def test_insert_overlapping_two(self):
        self.assertEqual(
            self.sut.insert([[1, 2], [3, 4]], [2, 5]),
            [[1, 5]])

    def test_insert_into_empty(self):
        self.assertEqual(
            self.sut.insert([], [2, 5]),
            [[2, 5]])

    def test_insert_at_start(self):
        self.assertEqual(
            self.sut.insert([[2, 5]], [0, 0]),
            [[0, 0], [2, 5]])


if __name__ == '__main__':
    unittest.main()
