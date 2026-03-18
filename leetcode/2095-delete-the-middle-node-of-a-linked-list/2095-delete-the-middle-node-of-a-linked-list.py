# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(not head.next):
            return None
        fast = head
        slow = head
        too_slow = ListNode(-1)
        while(fast and fast.next):
            fast=fast.next.next
            too_slow = slow 
            slow  = slow.next
        
        too_slow.next = slow.next
        return head
        