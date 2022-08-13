from pip import List

class Solution:
    def trap(self, height: List[int]) -> int:
        def peaks() -> List[int]: # list of peaks
            if len(height) < 3:
                return [[], []]
            pks = []
            i = 0
            while i < len(height) - 1:
                while i < len(height) - 1 and height[i] <= height[i+1]: # skip all inclines/flatground
                    i += 1
                pks.append(height[i]) # found peak
                while i < len(height) - 1 and height[i] >= height[i+1]: # skip all declines/flatground
                    i += 1
                i += 1
            return pks
        
        trapped_water = 0
        pks = peaks() # determine list of peaks
        pks_sorted = sorted(pks) # sort in ascending order
        height_iter = iter(height)
        try:
            curr = next(height_iter)
            while curr != pks[0]: # skip until you reach first peak
                curr = next(height_iter)
            for pk in pks[1:]:
                if pk < pks_sorted[-1]: # go until you find a peak greater than or equal to this peak
                    height_outer = pk # heights of outer columns
                    pks_sorted.remove(height_outer) # maintain sorted pks list
                else: # next peak is pks_sorted[-1], not something greater than or equal to original peak
                    height_outer = pks_sorted.pop() # set height_outer to largest peak remaining and maintain the sorted pks list
                
                while curr <= height_outer:
                    curr = next(height_iter)
                    trapped_water += height_outer - curr # add depth of water
                    print(f"trapped_water: {trapped_water}")
            return trapped_water
        except StopIteration as e:
            return trapped_water
        


# example 1
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution().trap(height))

