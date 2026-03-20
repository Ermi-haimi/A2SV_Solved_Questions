class Solution:
    def alternateDigitSum(self, n: int) -> int:
        ns = str(n)
        l=len(ns)
        pos= 1
        if(l%2==0):
            pos=-1
        
        ans = 0
        for i in range(l):
            curr = n%10
            n=n//10
            ans += pos*curr
            pos=-1*pos
        return ans

        
