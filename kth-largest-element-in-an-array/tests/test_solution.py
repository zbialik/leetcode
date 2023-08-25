import unittest

from solution.main import Solution

class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().findKthLargest(nums = [3,2,1,5,6,4], k = 2), 5)
    def test2(self):
        self.assertEqual(Solution().findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4), 4)


if __name__ == '__main__':
    unittest.main()
