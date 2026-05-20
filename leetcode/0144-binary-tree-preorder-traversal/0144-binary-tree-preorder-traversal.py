# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        st = []
        if(not root):
            return ans
        st.append(root)
        while(st):
            temp = st.pop() 
            ans.append(temp.val)
            if(temp.right):
                st.append(temp.right)
            if(temp.left):
                st.append(temp.left)
            
        return ans
