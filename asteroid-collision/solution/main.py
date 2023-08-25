from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        out = []
        # iterate until you get to positive directions
        #    append to out as you go

        # set left pointer to first positive asteroid
        # iterate right pointer until you reach negative
        #   append to out as you go
        #   c = r
        #   while asteroid[c] bigger asteroid[c-1]:
        #       out.pop()
        #       check next one 

        # then 
