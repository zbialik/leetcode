import unittest

from solution.main import Solution

class TestSolution(unittest.TestCase):
    def test1(self):
        print(f"input: '23'")
        self.assertCountEqual(Solution().letterCombinations("23"), ["ad","ae","af","bd","be","bf","cd","ce","cf"])
    def test2(self):
        print(f"input: ''")
        self.assertCountEqual(Solution().letterCombinations(""), [])
    def test3(self):
        print(f"input: '2'")
        self.assertCountEqual(Solution().letterCombinations("2"), ["a","b","c"])

if __name__ == '__main__':
    unittest.main()
