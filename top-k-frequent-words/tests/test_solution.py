import unittest

from solution.main import Solution

class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertListEqual(Solution().topKFrequent(words = ["i","love","leetcode","i","love","coding"], k = 2), ["i","love"])
    def test2(self):
        self.assertListEqual(Solution().topKFrequent(words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4), ["the","is","sunny","day"])


if __name__ == '__main__':
    unittest.main()
