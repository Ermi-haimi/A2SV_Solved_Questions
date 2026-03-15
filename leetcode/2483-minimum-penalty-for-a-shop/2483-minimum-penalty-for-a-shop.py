class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n=len(customers)
        ycount = 0
        for i in range(n):
            if(customers[i] == 'Y'):
                ycount+=1
        mn = ycount
        ans  = 0
        pen = ycount
        for i in range(n):
            if(customers[i] == 'Y'):
                pen-=1
                if(pen < mn):
                    ans=i+1
                    mn=pen
                if(pen==mn):
                    ans
            else:
                pen+=1
        return ans



        