from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd = defaultdict(int)
        td = defaultdict(int)
        n =len(s)
        if(n!=len(t)):
            return False
        for i in range(n):
            sd[s[i]]+=1
            td[t[i]]+=1
        for ch in s:
            if(sd[ch] != td[ch]):
                return False

        return True