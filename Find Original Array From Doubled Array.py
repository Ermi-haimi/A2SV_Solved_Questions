from collections import Counter
class Solution:
    def findOriginalArray(self, changed):
        original = []
        if len(changed)%2 != 0:
            return original
        freq = Counter(changed)
        changed.sort()

        for num in changed:
            if num in freq and freq[num] >0:
                if (num ==0):
                    if (freq[num] >1):
                        freq[num]-=1
                        freq[num*2] -=1
                        original.append(num)
                elif( num*2 in freq and freq[num*2] >0):
                    freq[num]-=1
                    freq[num*2] -=1
                    original.append(num)

        if(len(original)==len(changed)/2 ):
            return original
        return []




        
        