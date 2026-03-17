from collections import Counter
from math import ceil
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        rabbit = Counter(answers)
        ans =0
        for key,val in rabbit.items():
            
            if val >key+1:
                a = val/(key+1)
                a=ceil(a)
                ans+=a*(key+1)
            else:

                ans+=key+1
        return ans
                
