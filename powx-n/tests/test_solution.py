import unittest

from solution.main import Solution

class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertAlmostEqual(Solution().myPow(x = 2.00000, n = 10), 1024.00000)
    def test2(self):
        self.assertAlmostEqual(Solution().myPow(x = 2.10000, n = 3), 9.26100)
    def test3(self):
        self.assertAlmostEqual(Solution().myPow(x = 2.00000, n = -2), 0.25000)


if __name__ == '__main__':
    unittest.main()
