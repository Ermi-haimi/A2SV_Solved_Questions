# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        nums = []
        def dfs(nod,nahoo):
            if not nod:
                return 0
            nahoo = nahoo*10+nod.val
            if(not nod.left and not nod.right):
                return nahoo
            return dfs(nod.left,nahoo) + dfs(nod.right,nahoo)
            
        return dfs(root,0)
         

            

                
        