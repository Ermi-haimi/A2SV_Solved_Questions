# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count = 0
        mx = 0
        def inorder(nod):
            nonlocal count
            nonlocal mx
            if(nod):
                count+=1
                mx = max(count,mx)
                inorder(nod.left)
                inorder(nod.right)
                count-=1
        inorder(root)
        return mx
        