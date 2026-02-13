from math import ceil
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        same_xy = 0
        same_yx = 0
        for i in range(len(s1)):
            if(s1[i] == "x" and s2[i] =="y"):
                same_xy+=1
            elif(s1[i] == "y" and s2[i] =="x"):
                same_yx+=1
        
        if((same_xy+same_yx)%2!=0):
            return -1
        return same_xy//2 + same_yx//2 + same_xy%2 + same_yx%2