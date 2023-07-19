# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #time complexity: o(n)
        
        #idea: once fast.next is None slow will be at halfway point of LL
        
        #slice first half of linkedlist
        slow, fast = head, head.next
        while fast and fast.next: #fast will be None when odd and fast.next when even
            slow=slow.next
            fast=fast.next.next
        
        
        
        #reverse the second half of linkedlist 
        second=slow.next
        prev=slow.next=None
        while second:
            tmp=second.next
            second.next=prev
            prev=second
            second=tmp
        #second will be None since that pointer reached the end of the LL
        #prev will now store the proper head of the LL
        
        #merge lists
        first, second = head, prev
        while second: 
            tmp1, tmp2 = first.next, second.next
            first.next=second
            second.next=tmp1
            first, second = tmp1, tmp2
            
            
    
        
            
        
            
            
            
        