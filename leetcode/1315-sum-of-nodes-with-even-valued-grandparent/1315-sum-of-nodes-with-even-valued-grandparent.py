# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        count=0
        def search(nod,arr):
            nonlocal count
            if(not nod):
                arr.append(-1)
                return
            if(len(arr)>=2):
                if(arr[-2]%2 == 0):
                    count+=nod.val
            arr.append(nod.val)
            search(nod.left,arr)
            arr.pop()
            search(nod.right,arr)
            arr.pop()
        
        search(root,[])
        return count