# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(not head):
            return head
        odd = head
        even = head.next
        even_head = even
        pre_odd = None
        while(odd and even):
            pre_odd = odd
            odd.next = even.next
            odd = odd.next
            if(odd):
                even.next = odd.next
                even = even.next
        if odd:
            odd.next = even_head
        else:
            pre_odd.next = even_head
        return head
        

        