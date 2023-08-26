import unittest

from solution.main import Solution

class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertTrue(Solution().isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"))
    def test2(self):
        self.assertFalse(Solution().isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"))
    def test3(self):
        self.assertTrue(Solution().isInterleave(s1 = "", s2 = "", s3 = ""))


if __name__ == '__main__':
    unittest.main()
