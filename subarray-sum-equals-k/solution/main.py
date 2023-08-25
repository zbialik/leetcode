from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        l = len(nums)

        def countSubSum(i:int, j:int, count:int, layer:int) -> int:
            tab = "\t" * layer
            subsum = sum(nums[i:j])
            print(f"{tab} calculating sum for nums[{i}:{j}] --> sum of {nums[i:j]} is {subsum}")
            if subsum == k:
                count += 1
                print(f"{tab} subsum equals k --> count = {count}")
            if j < l:
                print(f"{tab} j < l --> count += countSubSum({i}, {j+1}, {count}, {layer+1})")
                count = countSubSum(i, j+1, count, layer+1)
            if i < j:
                print(f"{tab} i < j --> count += countSubSum({i+1}, {j}, {count}, {layer+1})")
                count = countSubSum(i+1, j, count, layer+1)
            return count
        
        return countSubSum(0,1,0,0)
