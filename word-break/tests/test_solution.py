import unittest

from solution.main import Solution

class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().wordBreak(s = "leetcode", wordDict = ["leet","code"]), True)
    def test2(self):
        self.assertEqual(Solution().wordBreak(s = "applepenapple", wordDict = ["apple","pen"]), True)
    def test3(self):
        self.assertEqual(Solution().wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]), False)
    def test4(self):
        self.assertEqual(Solution().wordBreak(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]), False)
        

if __name__ == '__main__':
    unittest.main()
