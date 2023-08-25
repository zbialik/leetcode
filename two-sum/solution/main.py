from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] <= target:
                for j in range(i,len(nums)):
                    if nums[i] + nums[j] == target:
                        return [i,j]
        