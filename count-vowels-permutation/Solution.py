from typing import List

# Given an integer n, your task is to count how many strings of length n can be formed under the following rules:
    # Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
    # Each vowel 'a' may only be followed by an 'e'.
    # Each vowel 'e' may only be followed by an 'a' or an 'i'.
    # Each vowel 'i' may not be followed by another 'i'.
    # Each vowel 'o' may only be followed by an 'i' or a 'u'.
    # Each vowel 'u' may only be followed by an 'a'.

# Since the answer may be too large, return it modulo 10^9 + 7.

# Constraints:
    # 1 <= n <= 2 * 10^4

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10 ** 9 + 7
        def countVowels(currVowels: List[str], count: int, i: int) -> int:
            nextVowelsMap = {
                'a': ['e'],
                'e': ['a', 'i'],
                'i': ['a', 'e', 'o', 'u'],
                'o': ['i', 'u'],
                'u': ['a']
            }
            if i == n:
                return len(currVowels)
            else:
                currCount = 0
                for vowel in currVowels:
                    currCount += countVowels(nextVowelsMap[vowel], count, i+1)
                return count + currCount
        
        currVowels = ['a', 'e', 'i', 'o', 'u']
        return countVowels(currVowels, 0, 1) % mod # hack solution -- should account for inside recursive function

# example
for n in [1, 2, 5]:
    out = Solution().countVowelPermutation(n=n)
    print(f"n={n} --> {out} permutations")
