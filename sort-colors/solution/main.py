from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numsCount = {
            0: 0,
            1: 0,
            2: 0
        }
        for n in nums:
            numsCount[n] += 1
        nums[:] = [0] * numsCount[0] + [1] * numsCount[1] + [2] * numsCount[2]
