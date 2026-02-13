class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patt = {}
        s = s.split(" ")
        seen = set()
        if(len(s) != len(pattern)):
            return False
        for ind,char in enumerate(pattern):
            if char in patt:
                if(s[ind] != patt[char]):
                    return False
            else:
                if(s[ind] in seen):
                    return False
                patt[char] = s[ind]
                seen.add(s[ind])
                
        
        return True