from collections import defaultdict
class Solution:
    def topKFrequent(self, nums, k):
        freq = defaultdict(int)
        for num in nums:
            freq[num]+=1
        
        freq = dict(sorted(freq.items(), key=lambda item:item[1], reverse=True))
        ans = []
        for key,value in freq.items():
            ans.append(key)
            if(len(ans) ==k):
                break
    
        return ans[0:k]