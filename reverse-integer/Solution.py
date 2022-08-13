from math import floor
from typing import List

class Solution:
    def reverse(self, x: int) -> int:
        lowerBound = -2147483648 # -2^31
        upperBound = 2147483647 # 2^31 - 1

        2147483647
        746

        # construct digitsArray for reverse number
        def numToDigitsArray(x: int, negative: bool) -> List[int]:
            units = 10
            digitsArray = []
            if negative:
                x = abs(x)
            while x >= units:
                units *= 10
            units /= 10 # to start at correct units place
            d = 0
            while units != 1:
                d = floor(x/units)
                x -= d * units
                digitsArray.append(d)
                units /= 10
            # append last digit (x in units place now)
            digitsArray.append(floor(x))
            return digitsArray
        
        # construct reverseNumber
        def reverseDigitsArray(digitsArray: List[int], negative: bool) -> int:
            def crawlReverse(i, units, reverseNumber):
                while i >= 0:
                    d = digitsArray[i]
                    reverseNumber = reverseNumber - d*units if negative else reverseNumber + d*units
                    units /= 10
                    i -= 1
                return reverseNumber

            if negative:
                boundaryArray = numToDigitsArray(lowerBound, True)
            else:
                boundaryArray = numToDigitsArray(upperBound, False)
            
            if len(digitsArray) == len(boundaryArray):
                digitsLength = len(digitsArray)
                i = digitsLength - 1; j = 0
                units = 10 ** (digitsLength - 1)
                reverseNumber = 0
                checkDigitBoundary = True
                while i >= 0 and checkDigitBoundary:
                    d = digitsArray[i]; b = boundaryArray[j]
                    if d <= b:
                        reverseNumber = reverseNumber - d*units if negative else reverseNumber + d*units
                        units /= 10
                        checkDigitBoundary = False if d < b else True
                        i -= 1
                        j += 1
                    else:
                        return 0
                return round(crawlReverse(i, units, reverseNumber))
            elif len(digitsArray) < len(boundaryArray):
                digitsLength = len(digitsArray)
                i = digitsLength - 1
                units = 10 ** (digitsLength - 1)
                reverseNumber = 0
                return round(crawlReverse(i, units, reverseNumber))
            else:
                return 0 # reverse will be outta bounds
        
        if x == 0 or x <= lowerBound: # edge case
            return 0
        else:
            negative = x < 0
        
        digitsArray = numToDigitsArray(x, negative) # e.g. 2130 --> [2, 1, 3, 0]
        while digitsArray[-1] == 0: # remove trailing zeros
            digitsArray.pop()
        
        return reverseDigitsArray(digitsArray, negative)
        
print()
solution = Solution()
# inputs = [12345, 54321, -12345, -54321, 1230, 12301, -2147483648]
inputs = [-2147483641, 2147483641]
for x in inputs:
    print(f"x = {x} --> reversed = {solution.reverse(x)}")
