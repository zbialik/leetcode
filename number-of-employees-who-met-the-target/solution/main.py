from typing import List
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        out = 0
        for h in hours:
            if h >= target:
                out += 1
        return out 