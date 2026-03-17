# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        buddy = ListNode(-1)
        buddy.next = head
        mover_head = head
        connector = buddy
        st = []
        while(mover_head):
            while(st and mover_head.val >st[-1]):
                st.pop()
            st.append(mover_head.val)
            mover_head=mover_head.next
        
        for num in st:
            connector.next = ListNode(num)
            connector = connector.next
        return buddy.next
        

        return buddy.next 

