from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1
        
        i = 1; always_increase = True
        while i <= len(nums) - 2:
            p = nums[i-1]; c = nums[i]; n = nums[i+1]
            if c > p and c > n:
                return i 
            elif c > n:
                always_increase = False
                i+=1
            else:
                i+=1
        return i if always_increase else 0
        