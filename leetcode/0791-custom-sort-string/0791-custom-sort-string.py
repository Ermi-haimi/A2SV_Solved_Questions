from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_c = Counter(s)
        ans =[]
        pointer = 0
        for c in order:
            if(c in s_c):
                pointer +=1 
                temp = c*s_c[c]
                s_c[c]=0
                ans.append(temp)
        
        for key,val in s_c.items():
            if(val > 0):
                temp = key*val
                ans.append(temp)
        
        return "".join(ans)



        


