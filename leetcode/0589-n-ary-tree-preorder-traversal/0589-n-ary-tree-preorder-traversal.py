"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        def pren(nod):
            if(not nod):
                return
            else:
                ans.append(nod.val)
                for n in nod.children:
                    pren(n)
        
        pren(root)
        return ans