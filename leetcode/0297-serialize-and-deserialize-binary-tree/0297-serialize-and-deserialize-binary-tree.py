# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def ser(self,nod,arr):
        if(nod == None):
            arr.append('None')
            return
        arr.append(str(nod.val))
        self.ser(nod.left,arr)
        self.ser(nod.right,arr)

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        store = []
        self.ser(root,store)
        return ",".join(store)
        

    def des(self,st):
        val = st.pop()
        if(val[0] == 'N'):
            return None
        rot = TreeNode(int(val))
        rot.left = self.des(st) 
        rot.right = self.des(st) 
        
        return rot

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        man = data.split(',')
        man.reverse()
        ans = self.des(man)
        return ans


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))