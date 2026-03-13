class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        pre = [0 for _ in range(n)]
        for arr in shifts:
            l,r,k = arr
            if(k ==0):
                k=-1
            pre[l] +=k
            if(r<n-1):
                pre[r+1] += -k
        
        for i in range(1,n):
            pre[i] = pre[i]+pre[i-1]
            
        s = list(s)
        for i in range(n):
            curr = ord(s[i])
            curr+=pre[i]
            new_p = ord('a')+((curr-ord('a'))%26)
            s[i] = chr(new_p)
        return "".join(s) 

        