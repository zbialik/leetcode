import unittest

from solution.main import Solution

class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().isPalindrome(s = "A man, a plan, a canal: Panama"), True)
    def test2(self):
        self.assertEqual(Solution().isPalindrome(s = "race a car"), False)
    def test3(self):
        self.assertEqual(Solution().isPalindrome(s = " "), True)


if __name__ == '__main__':
    unittest.main()
