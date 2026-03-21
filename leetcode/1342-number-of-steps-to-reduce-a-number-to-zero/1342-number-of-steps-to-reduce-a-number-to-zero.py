class Solution:
    def numberOfSteps(self, num: int) -> int:
        def count(n, step):
            if(n == 0):
                return step
            
            if(n%2 == 0):
                return count(n/2, step+1)
            else:
                return count(n-1, step+1)
        
        ans = count(num,0)
        return ans
            