import unittest

from solution.main import Solution

class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertListEqual(Solution().twoSum(nums = [2,7,11,15], target = 9),  [0,1])
    def test2(self):
        self.assertListEqual(Solution().twoSum(nums = [2,7,11,15], target = 9), [1,2])
    def test3(self):
        self.assertListEqual(Solution().twoSum(nums = [2,7,11,15], target = 9), [0,1])

if __name__ == '__main__':
    unittest.main()
