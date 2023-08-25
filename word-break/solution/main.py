from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # remove repeated strings from wordDict
        def repeating_substring(s):
            n = len(s)
            substring = ""
            for i in range(n):
                substring += s[i]
                if substring * (n//len(substring)) == s:
                    return substring
            return None
        wordDictNew = []
        for w in wordDict:
            w2 = repeating_substring(w)
            if w2 not in wordDictNew:
                wordDictNew.append(w2) 
        
        def words(sub_s:str):
            for w in wordDictNew:
                if w == sub_s:
                    return True
                else:
                    if w in sub_s:
                        out = words(sub_s[sub_s.index(w) + len(w):])
                        if out:
                            return out
            return False
        return words(s)
