class Solution:
    def countKeyChanges(self, s: str) -> int:
        s=s.lower()
        n = len(s)
        ans=0
        for i in range(0,n-1):
            if(s[i] != s[i+1]):
                ans+=1
        return ans