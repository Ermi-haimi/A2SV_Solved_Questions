# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(not head or not head.next):
            return head
        one = None
        two = head
        three = head.next
        while(two):
            two.next = one
            one = two
            two=three
            if(three):
                three = three.next
            
        return one
        