import solution
import unittest


class Test_TestSolution(unittest.TestCase):
    def setUp(self):
        self.sut = solution.Solution()

    def test_foo(self):
        self.assertEqual(self.sut.foo(), "bar")


if __name__ == '__main__':
    unittest.main()
