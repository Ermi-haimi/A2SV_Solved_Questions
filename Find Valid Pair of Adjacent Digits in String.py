from collections import Counter
class Solution:
    def findValidPair(self, s: str) -> str:
        freq = Counter(s)
        left = 0
        right = 1
        ans = ""
        while(right <len(s)):
            if(s[left] != s[right]):
                l_num = int(s[left])
                r_num = int(s[right])
                if(freq[s[left]] ==l_num and freq[s[right]] ==r_num):
                    ans = s[left:right+1]
                    break
            left+=1
            right+=1
        
        return ans