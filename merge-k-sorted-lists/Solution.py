from tkinter import N
from typing import Optional
from pip import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dict = {}
        for n in lists:
            while n != None:
                try:
                    dict[n.val].append(n.val)
                except:
                    dict[n.val] = [n.val]
                n = n.next
        
        sortedDictKeys = sorted(dict.keys())
        if len(sortedDictKeys) == 0:
            return
        else:
            headVal = dict[sortedDictKeys[0]].pop()
            head = ListNode(val=headVal)
            n = head # initialize pointer to head
        
        for i in sortedDictKeys:
            vals = dict[i]
            for val in vals:
                n.next = ListNode(val=val)
                n = n.next # move pointer to next ListNode
        return head

# example 1
lists = [[1,4,5],[1,3,4],[2,6]]
print(Solution().mergeKLists(lists))
