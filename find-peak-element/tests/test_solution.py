import unittest

from solution.main import Solution

class TestSolution(unittest.TestCase):
    def test1(self):
        print(f"input: [1,2,3,1]")
        self.assertEqual(Solution().findPeakElement([1,2,3,1]), 2)
    def test2(self):
        print(f"input: [1,2,1,3,5,6,4]")
        self.assertTrue(Solution().findPeakElement([1,2,1,3,5,6,4]) in [5, 1])
    def test3(self):
        print(f"input: [3,2,1] --> {Solution().findPeakElement([3,2,1])}")
        self.assertTrue(Solution().findPeakElement([3,2,1]) in [0])

if __name__ == '__main__':
    unittest.main()
