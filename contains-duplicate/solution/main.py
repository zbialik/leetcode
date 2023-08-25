from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check = {}
        i = 0
        while i < len(nums):
            if check.get(nums[i]):
                return True 
            else:
                check[nums[i]] = 1
            i += 1
        return False
    