from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        out = 0

        def isDivisible(amt:int, c:int) -> bool:
            return amt % c == 0

        def find_divisor(i:int) -> int:
            divisor = 0
            c = coins[i]
            remaining = amount // c # start with highest divisor
            ci = i+1
            while ci < len(coins) and remaining != 0:
                

            return divisor

        # amount = sum(coins[i] * x[i]) for i in range(len(coins))
        for c in coins:
            mult = amount // c 
            divisible = False
            while not divisible:
                mult -= 1
                # check if divisible
                for 

                # amount - (c * mult)

            out += amount // c
            amount = amount % c
        return out if amount == 0 else -1
    