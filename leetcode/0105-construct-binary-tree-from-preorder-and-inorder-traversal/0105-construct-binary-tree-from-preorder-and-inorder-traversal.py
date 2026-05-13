# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # root = TreeNode(preorder[0])
        # mover = root
        # visited = set([preorder[0]])
        # keeper = root
        # p = 0
        # i = 0
        # n = len(preorder)
        def constructBT(preo,ino):
            if(len(preo) == 0):
                return None
            head = TreeNode(preo[0])
            i = 0
            while(i<len(ino) and ino[i] != preo[0]):
                i+=1
            if(i<len(ino)):
                head.left = constructBT(preo[1:i+1],ino[:i])
                head.right = constructBT(preo[i+1:],ino[i+1:])

            return head
        
        ans = constructBT(preorder,inorder)
        return ans
