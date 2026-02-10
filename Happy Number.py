class Solution:
    def isHappy(self, n: int) -> bool:
        if(n == 1 or n==7):
            return True
        if(n>1 and n<=9):
            return False
        m=0
        while(n >0):
            curr =n%10
            m+=curr**2
            n=n//10
        m+=n**2
        return self.isHappy(m)