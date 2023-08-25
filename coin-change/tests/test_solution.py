import unittest

from solution.main import Solution

class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().coinChange(coins = [1,2,5], amount = 11), 3)
    def test2(self):
        self.assertEqual(Solution().coinChange(coins = [2], amount = 3), -1)
    def test3(self):
        self.assertEqual(Solution().coinChange(coins = [1], amount = 0), 0)
    def test4(self):
        self.assertEqual(Solution().coinChange(coins = [186,419,83,408], amount = 6249), 20)


if __name__ == '__main__':
    unittest.main()
