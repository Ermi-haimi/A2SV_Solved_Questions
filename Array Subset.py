#User function Template for python3
from collections import Counter

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        da = Counter(a)
        db = Counter(b)
        for key in db:
            if(key in da):
                if( db[key] > da[key] ):
                    return False
            else:
                return False
        
        return True