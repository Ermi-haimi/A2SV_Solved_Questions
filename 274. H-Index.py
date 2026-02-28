class Solution:
    def hIndex(self, citations) -> int:
        mx = 0
        citations = sorted(citations, reverse=True)
        for i in range(len(citations)):
            if(i+1 <= citations[i]):
                mx = i+1
            else:
                break
        
        return mx