# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p1 = []  
        q1 = []
        def pre(nod,arr):
            if(not nod):
                arr.append(None)
                return
            arr.append(nod.val)
            pre(nod.left,arr)
            pre(nod.right,arr)
        
        pre(p,p1)
        pre(q,q1)
        pn = len(p1)
        qn = len(q1)
        if(qn != pn):
            return False
        for i in range(pn):
            if(p1[i]!=q1[i]):
                return False
        return True
          