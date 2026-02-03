class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_l=100000000000
        for word in strs:
            min_l = min(min_l, len(word))
        
        ans = ""
        strs_l = len(strs)
        broke = False
        for i in range(min_l):
            curr = strs[0][i]
            for j in range(1,strs_l):
                if(strs[j][i] != curr):
                    broke = True
                    break
            if(broke):
                break
            else:
                ans+=curr
        return ans
        