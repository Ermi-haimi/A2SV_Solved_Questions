from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        freq = dict(sorted(freq.items(), reverse=True, key=lambda item:item[1]))

        ans = ""
        for key,val in freq.items():
            ans+=key*val
        
        return ans