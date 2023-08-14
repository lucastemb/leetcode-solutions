# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr=head
        visit=set()
        while curr != None:
            if curr in visit: 
                return True
            visit.add(curr)
            curr=curr.next
        return False