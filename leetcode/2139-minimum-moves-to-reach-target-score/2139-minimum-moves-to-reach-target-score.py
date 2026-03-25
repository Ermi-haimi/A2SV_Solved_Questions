from math import ceil
class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        def counter(num,doub):
            nonlocal count
            if(num == 1):
                return
            if doub>0:
                count+=1
                if(num%2 == 0):
                    counter(num/2,doub-1)
                else:
                    count+=1
                    counter(num//2,doub-1)
            else:
                count+=num-1
        counter(target,maxDoubles)
        return int(count)
