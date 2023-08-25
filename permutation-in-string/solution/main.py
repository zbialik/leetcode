from typing import List
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def permutations(s):
            for c in s:
                s += c
                permutations(s)
        perms = permutations("", s1)
        for perm in perms:
            if perm in s2:
                return True
        return False
        