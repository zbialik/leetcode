from calendar import c
from re import A
from pip import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        charMap = {
            '2': ["a", "b", "c"],
            '3': ["d", "e", "f"],
            '4': ["g", "h", "i"],
            '5': ["j", "k", "l"],
            '6': ["m", "n", "o"],
            '7': ["p", "q", "r", "s"],
            '8': ["t", "u", "v"],
            '9': ["w", "x", "y", "z"]
        }
        combos = charMap[digits[0]]

        for digit in digits[1:]:
            chars = charMap[digit]
            charIter = iter(chars)
            n = next(charIter)
            l = len(combos)
            combos = combos * len(chars) # prepare duplicate options for appending diff letters
            i = 0
            for j in range(len(combos)):
                if i >= l:
                    n = next(charIter)
                    i = 0
                combos[j] += n
                i += 1
        return combos


# example 1
digits = "2"
print(Solution().letterCombinations(digits))
