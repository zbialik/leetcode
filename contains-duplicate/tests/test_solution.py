import unittest

from solution.main import Solution

class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().containsDuplicate(nums = [1,2,3,1]), True)
    def test2(self):
        self.assertEqual(Solution().containsDuplicate(nums = [1,2,3,4]), False)
    def test3(self):
        self.assertEqual(Solution().containsDuplicate(nums = [1,1,1,3,3,4,3,2,4,2]), True)

if __name__ == '__main__':
    unittest.main()
