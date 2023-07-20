# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes={}
        curr=head
        while curr:
            if curr in nodes:
                return True
            nodes[curr]=1+nodes.get(curr,0)
            curr=curr.next
        return False