class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
        def okay(mx):
            if(mx<max(weights)):
                return False
            count = 0
            w = 0
            for i in range(n):
                w+=weights[i]
                if(w==mx):
                    print(mx,w)
                    w = 0
                    count+=1
                elif(w>mx):
                    print(mx,w-weights[i])
                    if(i == n-1):
                        count+=1
                    w=weights[i]
                    count+=1
                elif(i==n-1):
                    count+=1
            print(mx,count,days)
            return count <= days
        
        r = sum(weights)
        l =0
        ans = -1
        while(l<=r):
            m = l+(r-l)//2
            if(okay(m)):
                ans = m
                print(ans)
                r = m-1
            else:
                l = m+1
        return ans
