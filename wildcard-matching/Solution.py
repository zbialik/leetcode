from typing import List


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # organize p into patterns to compare chars in s against
        # e.g. p = 'aa*b??***cccc' --> patterns = ['aa', 'b??', 'cccc']
        def constructHardPatterns(p) -> List:
            patterns = []
            if len(p) == 0:
                return []
            elif len(p) == 1:
                return [p[0]]
            
            # set first hard pattern to '*' to account for when p is '***'
            h = p[0]
            if h == '*':
                patterns.append(h)
                h = ''
            
            for cp in p[1:]:
                if cp == '*':
                    if h != '':
                        patterns.append(h)
                    h = ''
                else:
                    h += cp
            
            if h != '': # add final hard pattern
                patterns.append(h)
            elif cp == '*':
                patterns.append(cp)
            
            return patterns
        
        def matchPattern(s1, p1):
            if p1 == '*':
                return True
            if len(s1) != len(p1):
                return False
            else:
                for i in range(len(s1)):
                    cs = s1[i]; cp = p1[i]
                    if cp != cs and cp != '?':
                        return False
                return True

        # recursive search
        def compare(s, patterns, si, pi):
            prefixPattern = patterns[pi] # shouldn't go out of boundary
            
            if si == len(s): # False if exceeded length of s
                return prefixPattern == '*' 
            
            # TODO: DELETE
            # if pi == len(patterns) - 1:
            #     return matchPattern(s[si:], prefixPattern)
            
            if len(s[si:]) >= len(prefixPattern): 
                subString = s[si:si+len(prefixPattern)]
                match = matchPattern(subString, prefixPattern) # compare section of s against prefixPattern
                if match:
                    if len(patterns) == pi + 1:
                        if matchPattern(s[si:], prefixPattern):
                            return True
                        else:
                            return compare(s, patterns, si + 1, pi)
                    else:
                        return compare(s, patterns, si + len(prefixPattern), pi + 1)
                else:
                    return compare(s, patterns, si + 1, pi)
            else:
                return False

        print(f"INPUTS: ")
        print(f"\t s = {s} \n\t p = {p} \n")
        patterns = constructHardPatterns(p)
        print(f"generated patterns = {patterns}")

        # case 1: len(patterns) == 0
        if len(patterns) == 0:
            if len(s) == 0:
                return True
            else:
                return False
        
        prefixPattern = patterns.pop(0)
        if len(patterns) == 0: # was a length of 1
            if matchPattern(s, prefixPattern):
                return True
            else:
                return False
        
        # case 2: patterns[0] != '*'
        if prefixPattern != '*':
            if matchPattern(s[0:len(prefixPattern)], prefixPattern):
                s = s[len(prefixPattern):]
                if len(patterns) == 0: 
                    if len(s) == 0:
                        return True
                    else:
                        return False
                else:
                    return compare(s, patterns, 0, 0) # execute recursive search
            else:
                return False
        # case 3: patterns[0] == '*'
        else:
            return compare(s, patterns, 0, 0) # execute recursive search
        

# example 1
s = "aaaa"; p = "*aaaaa"
out = Solution().isMatch(s=s, p=p)
if out:
    print(f"\n{s} matches pattern: {p}\n")
else:
    print(f"\n{s} does NOT match pattern: {p}\n")
