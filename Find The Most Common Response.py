from collections import defaultdict
class Solution:
    def findCommonResponse(self, responses):
        freq = defaultdict(int)
        for res in responses:
            seen = set()
            for r in res:
                if r not in seen:
                    seen.add(r)
                    freq[r]+=1
        max_count = -1
        ans = "zzzzzzzzzzzzzzzzzz"
        print(freq)
        for key, val in freq.items():
            if max_count< val:
                max_count = val
                ans = key
            elif(max_count == val):
                if ans>key:
                    ans = key
        return ans