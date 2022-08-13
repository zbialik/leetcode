# class Solution:
from pip import List

def maxArea(height: List[int]) -> int:
    maxArea = 0
    il = 0; ir = len(height)-1 # initialize left and right pointers
    # we will move left and right pointers inward until they touch
    while ir - il > 0:
        h = min(height[il], height[ir])
        w = ir - il
        currArea = h * w
        maxArea = max(maxArea, currArea)
        if height[il] > height[ir]: # move right pointer to the left
            ir -= 1
        elif height[ir] > height[il]: # move left pointer to the right
            il += 1
        else: # move both pointers inward
            ir -= 1; il += 1
    return maxArea

# example 1
height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))

# example 2

