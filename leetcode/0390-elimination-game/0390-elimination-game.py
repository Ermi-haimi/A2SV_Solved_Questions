class Solution:
    def lastRemaining(self, n: int) -> int:
        f = 1
        l = n
        c = n
        s = 1
        def helper(first,last,count,step,turn):
            if(count == 1):
                return first
            else:
                if(count%2 != 0):
                    first+=step
                    last-=step
                else:
                    if(turn):
                        first+=step
                    else:
                        last+=step
                return helper(first,last,count//2,step*2,not turn)
        
        ans = helper(f,l,c,s,True)
        return ans

            
