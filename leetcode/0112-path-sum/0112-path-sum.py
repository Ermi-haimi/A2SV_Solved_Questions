# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        sm = 0
        def dfs(nod,num):
            if not nod:
                return False
            # if num = = nod.val
            if(num==nod.val and not nod.left and not nod.right):
                return True
            
            ans = dfs(nod.left,num-nod.val)
            if(ans):
                return True
            ansR = dfs(nod.right,num-nod.val)
            if ansR:
                return True
            
            return False
        ans = dfs(root,targetSum)
        return ans
            
