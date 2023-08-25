from typing import List

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

        def get_combos(curr_combos:List[str], new_chars:List[str]):
            new_combos = []
            for curr_combo in curr_combos:
                for new_char in new_chars:
                    new_combos.append(curr_combo + new_char)
            return new_combos
        
        combos = charMap[digits[0]]
        
        for d in digits[1:]:
            new_chars = charMap[d]
            combos = get_combos(combos, new_chars)
        return combos
