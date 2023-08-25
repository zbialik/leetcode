from typing import List
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordsCount = {}
        wordsOrdered = []
        for w in words:
            if wordsCount.get(w):
                wordsCount[w] += 1
            else:
                wordsCount[w] = 1
        
        for w, count in wordsCount.items():
            if wordsOrdered:
                i = 0
                wo = wordsOrdered[i]
                while i < len(wordsOrdered) and (wordsCount[wo] > count or (wordsCount[wo] == count and wo < w)):
                    i += 1
                    if i < len(wordsOrdered):
                        wo = wordsOrdered[i]
                wordsOrdered.insert(i,w)
            else:
                wordsOrdered.append(w)
        return wordsOrdered[:k]

