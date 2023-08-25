import unittest

from solution.main import Solution

class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().coinChange(coins = [1,2,5], amount = 11), 3)


if __name__ == '__main__':
    unittest.main()
