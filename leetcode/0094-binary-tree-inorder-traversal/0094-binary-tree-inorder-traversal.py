# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def inorder(nod):
            if nod:
                inorder(nod.left)
                ans.append(nod.val)
                inorder(nod.right)
        
        inorder(root)
        return ans
