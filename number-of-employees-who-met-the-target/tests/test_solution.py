import unittest

from solution.main import Solution

class TestSolution(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution().numberOfEmployeesWhoMetTarget(hours = [0,1,2,3,4], target = 2), 3)
    def test_2(self):
        self.assertEqual(Solution().numberOfEmployeesWhoMetTarget(hours = [5,1,4,2,2], target = 6), 0)

if __name__ == '__main__':
    unittest.main()
