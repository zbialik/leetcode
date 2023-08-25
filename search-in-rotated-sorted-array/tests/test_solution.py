import unittest

from solution.main import Solution

class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().search(nums=[4,5,6,7,0,1,2], target=0), 4)
    def test2(self):
        self.assertEqual(Solution().search(nums=[4,5,6,7,0,1,2], target=3), -1)
    def test3(self):
        self.assertEqual(Solution().search(nums=[1], target=0), -1)

if __name__ == '__main__':
    unittest.main()
