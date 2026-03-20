class Solution:
    def digitSum(self, s: str, k: int) -> str:
        n=len(s)
        if(n<=k):
            return s
        new_s = ""
        for i in range(0,n,k):
            curr=0
            for j in range(i,i+k):
                if(j<n):
                    curr+=int(s[j])
            new_s+=str(curr)
        return self.digitSum(new_s,k)
        
