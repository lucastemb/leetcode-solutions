# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head 
        while curr:
            #temp will be pointing to (2) in the first case
            temp=curr.next
            
            #curr.next will point to None so (1).next equals to (0) [(0)->(1)]
            curr.next=prev

            #the previous one is now (1)
            prev=curr

            #current becomes (2) now 
            curr=temp
        
        #returning previous will return the entire reverse linked list
        return prev
    
