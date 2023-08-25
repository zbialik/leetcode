import unittest

from solution.main import Solution

class TestSolution(unittest.TestCase):
    # def test1(self):
    #     print(f"input: [1,1,1],2")
    #     self.assertEqual(Solution().subarraySum([1,1,1],2), 2)
    
    # def test2(self):
    #     print(f"input: [1,2,3],3")
    #     self.assertEqual(Solution().subarraySum([1,2,3],3), 2)
    
    def test3(self):
        print(f"input: [1,2,1,2,1],3")
        self.assertEqual(Solution().subarraySum([1,2,1,2,1],3), 4)

if __name__ == '__main__':
    unittest.main()
