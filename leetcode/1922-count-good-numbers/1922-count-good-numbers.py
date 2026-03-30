class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 7+10**9
        od = n//2
        ev = n-od
        def exp(num,ex):
            res = 1
            if(ex==0):
                return 1
            while(ex>1):
                if(ex%2 ==1):
                    res =(res*num)%mod
                    ex-=1
                else:
                    num = (num*num)%mod
                    ex=ex//2

            return (num*res)%mod
            

        ans = exp(5,ev)*exp(4,od)
        
        return ans%mod

