class Solution:
    def partitionLabels(self, s: str):
        last = {}
        for ind,c in enumerate(s):
            last[c] = ind

        i = 0
        ans = []
        curr = 0
        last_i = 0
        while(i<len(s)):
            curr = last[s[i]]

            while(i<=curr):
                if(last[s[i]] > curr):
                    curr = last[s[i]]
                i+=1
            
            ans.append(curr-last_i+1)
            last_i = i
            
        return ans