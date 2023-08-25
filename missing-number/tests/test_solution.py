import unittest

from solution.main import Solution

class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().missingNumber(nums = [3,0,1]), 2)
    def test2(self):
        self.assertEqual(Solution().missingNumber(nums = [0,1]), 2)
    def test3(self):
        self.assertEqual(Solution().missingNumber(nums = [9,6,4,2,3,5,7,0,1]), 8)


if __name__ == '__main__':
    unittest.main()
