import unittest

from solution.main import Solution

class TestSolution(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution().checkInclusion(s1 = "ab", s2 = "eidbaooo"), True)
    def test_2(self):
        self.assertEqual(Solution().checkInclusion(s1 = "ab", s2 = "eidboaoo"), False)

if __name__ == '__main__':
    unittest.main()
