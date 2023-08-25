from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numsCheck = list(range(len(nums)+1))
        for n in nums:
            numsCheck.remove(n)
        return numsCheck[0]