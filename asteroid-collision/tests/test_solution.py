import unittest

from solution.main import Solution

class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertListEqual(Solution().asteroidCollision(asteroids = [5,10,-5]), [5,10])
    def test2(self):
        self.assertListEqual(Solution().asteroidCollision(asteroids = [8,-8]), [])
    def test3(self):
        self.assertListEqual(Solution().asteroidCollision(asteroids = [10,2,-5]), [10])

if __name__ == '__main__':
    unittest.main()
